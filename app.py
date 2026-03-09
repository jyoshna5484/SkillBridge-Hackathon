from flask import Flask, render_template, request

app = Flask(__name__)

# Career database
careers = {
    "Software Developer": [
        "Python",
        "Data Structures",
        "Algorithms",
        "Git",
        "Databases",
        "Problem Solving"
    ],

    "Data Scientist": [
        "Python",
        "Statistics",
        "Machine Learning",
        "Data Visualization",
        "SQL",
        "Pandas"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git",
        "Web APIs"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Data Structures",
        "Math"
    ],

    "Cyber Security Specialist": [
        "Networking",
        "Linux",
        "Cryptography",
        "Ethical Hacking",
        "Security Tools"
    ],

    "UI/UX Designer": [
        "Figma",
        "Wireframing",
        "User Research",
        "Prototyping",
        "Design Principles"
    ],

    "Mobile App Developer": [
        "Java",
        "Kotlin",
        "Flutter",
        "Android Studio",
        "APIs"
    ],

    "DevOps Engineer": [
        "Linux",
        "Docker",
        "Kubernetes",
        "CI/CD",
        "Cloud Computing"
    ]
}

@app.route('/')
def home():
    return render_template("index.html", careers=careers.keys())

@app.route('/skills', methods=['POST'])
def skills():
    career = request.form['career']
    skills = careers[career]
    return render_template("skills.html", career=career, skills=skills)

@app.route('/result', methods=['POST'])
def result():

    career = request.form['career']
    required_skills = careers[career]

    user_skills = request.form.getlist('skills')

    completed = len(user_skills)
    total = len(required_skills)

    score = int((completed / total) * 100)

    missing_skills = list(set(required_skills) - set(user_skills))

    return render_template(
        "result.html",
        career=career,
        score=score,
        missing=missing_skills
    )

if __name__ == '__main__':
    app.run(debug=True)