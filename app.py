from flask import Flask, render_template, request

app = Flask(__name__)

# Career skill database
career_skills = {
    "Software Developer": ["Python", "Data Structures", "Git", "Databases", "Problem Solving"],
    "Data Scientist": ["Python", "Statistics", "Machine Learning", "Data Visualization", "SQL"],
    "UI Designer": ["Figma", "UX Principles", "Wireframing", "Prototyping", "User Research"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_career = None
    skills = []
    known_skills = []
    missing_skills = []
    readiness = 0

    if request.method == "POST":
        selected_career = request.form.get("career")
        skills = career_skills.get(selected_career, [])

        known_skills = request.form.getlist("skills")

        if skills:
            readiness = int((len(known_skills) / len(skills)) * 100)

        missing_skills = list(set(skills) - set(known_skills))

    return render_template(
        "index.html",
        careers=career_skills.keys(),
        selected_career=selected_career,
        skills=skills,
        known_skills=known_skills,
        missing_skills=missing_skills,
        readiness=readiness
    )

if __name__ == "__main__":
    app.run(debug=True)
career_skills = {
    "Software Developer": ["Python", "Data Structures", "Git", "Databases", "Problem Solving"],
    "Data Scientist": ["Python", "Statistics", "Machine Learning", "Data Visualization", "SQL"],
    "UI Designer": ["Figma", "UX Principles", "Wireframing", "Prototyping", "User Research"]
}