# ============================================================
#  SkillBridge — Flask Backend (app.py)
#  Run:  pip install flask
#        python app.py
#  Open: http://localhost:5000
# ============================================================

from flask import Flask, jsonify, request, render_template_string, send_from_directory
from skillbridge_data import CAREERS
import os, json

app = Flask(__name__)

# ── Helper: find career by id ────────────────────────────────
def find_career(career_id):
    return next((c for c in CAREERS if c["id"] == career_id), None)


# ════════════════════════════════════════════════════════════
#  API ROUTES  (called by the HTML frontend via fetch)
# ════════════════════════════════════════════════════════════

# GET /api/careers  →  returns all careers (id, icon, name, cat, desc)
@app.route("/api/careers")
def get_careers():
    data = [{"id":c["id"],"icon":c["icon"],"name":c["name"],
             "cat":c["cat"],"desc":c["desc"]} for c in CAREERS]
    return jsonify({"careers": data, "total": len(data)})


# GET /api/career/<id>  →  returns full career details
@app.route("/api/career/<career_id>")
def get_career(career_id):
    career = find_career(career_id)
    if not career:
        return jsonify({"error": "Career not found"}), 404
    return jsonify(career)


# POST /api/progress  →  send known skills, get back score + missing + roadmap
# Body: { "career_id": "swe", "known_skills": ["python", "git"] }
@app.route("/api/progress", methods=["POST"])
def get_progress():
    body       = request.get_json()
    career_id  = body.get("career_id", "")
    known      = set(body.get("known_skills", []))

    career = find_career(career_id)
    if not career:
        return jsonify({"error": "Career not found"}), 404

    total   = len(career["skills"])
    done    = sum(1 for s in career["skills"] if s["id"] in known)
    pct     = round((done / total) * 100)
    missing = [s for s in career["skills"] if s["id"] not in known]

    # build resources only for missing skills
    resources = {}
    for s in missing:
        name = s["name"]
        if name in career["resources"]:
            resources[name] = career["resources"][name]

    return jsonify({
        "career_id"     : career_id,
        "career_name"   : career["name"],
        "total_skills"  : total,
        "known_count"   : done,
        "readiness_pct" : pct,
        "missing_skills": missing,
        "roadmap"       : career["roadmap"],
        "resources"     : resources,
        "career_ready"  : pct == 100
    })


# GET /api/categories  →  returns all unique categories
@app.route("/api/categories")
def get_categories():
    cats = sorted(set(c["cat"] for c in CAREERS))
    return jsonify({"categories": cats})


# ════════════════════════════════════════════════════════════
#  SERVE FRONTEND
#  Put your skillbridge.html in the same folder as app.py
#  It will be served at http://localhost:5000
# ════════════════════════════════════════════════════════════

@app.route("/")
def index():
    # Serve skillbridge.html from same directory
    html_path = os.path.join(os.path.dirname(__file__), "skillbridge.html")
    if os.path.exists(html_path):
        with open(html_path, "r") as f:
            return f.read()
    return "<h2>Put skillbridge.html in the same folder as app.py</h2>", 404


# ════════════════════════════════════════════════════════════
#  RUN
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "="*50)
    print("  🌉  SkillBridge Flask Server Starting...")
    print(f"  📦  Loaded {len(CAREERS)} careers")
    print("  🌐  Open: http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
