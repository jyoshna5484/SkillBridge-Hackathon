from flask import Flask, render_template, request

app = Flask(__name__)

# Career and Required Skills Database
career_skills = {
    "Software Developer": [
        "Python",
        "Data Structures",
        "Algorithms",
        "Git",
        "Databases"
    ],

    "Data Scientist": [
        "Python",
        "Statistics",
        "Machine Learning",
        "SQL",
        "Data Visualization"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],

    "AI Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "Mathematics"
    ]
}

# Home Page (Career Selection)
@app.route('/')
def home():
    return render_template("index.html", careers=career_skills.keys())


# Show Required Skills
@app.route('/skills', methods=['POST'])
def skills():

    career = request.form['career']

    required_skills = career_skills[career]

    return render_template(
        "skills.html",
        career=career,
        skills=required_skills
    )


# Calculate Readiness Score
@app.route('/result', methods=['POST'])
def result():

    career = request.form['career']

    required_skills = career_skills[career]

    selected_skills = request.form.getlist('skills')

    total = len(required_skills)

    completed = len(selected_skills)

    score = int((completed / total) * 100)

    missing = list(set(required_skills) - set(selected_skills))

    return render_template(
        "result.html",
        career=career,
        score=score,
        missing=missing
    )


if __name__ == '__main__':
    app.run(debug=True)
career_skills = {

"Software Developer": [
"Python",
"Java",
"C++",
"Data Structures",
"Algorithms",
"Object Oriented Programming",
"Git",
"Databases",
"Problem Solving",
"Software Design"
],

"Software Engineer": [
"Programming (Java/Python/C++)",
"Data Structures",
"Algorithms",
"System Design",
"Version Control (Git)",
"Databases",
"Testing",
"Debugging"
],

"Frontend Developer": [
"HTML",
"CSS",
"JavaScript",
"React",
"Responsive Design",
"Web Accessibility",
"Git",
"UI Frameworks"
],

"Backend Developer": [
"Python",
"Java",
"Node.js",
"REST APIs",
"Databases",
"Server Management",
"Authentication",
"Microservices"
],

"Full Stack Developer": [
"HTML",
"CSS",
"JavaScript",
"React",
"Node.js",
"Databases",
"APIs",
"Git",
"Deployment"
],

"Web Developer": [
"HTML",
"CSS",
"JavaScript",
"Web Frameworks",
"Git",
"Responsive Design",
"Web Hosting",
"SEO Basics"
],

"Mobile App Developer": [
"Java",
"Kotlin",
"Flutter",
"Dart",
"Android Studio",
"APIs",
"Firebase",
"UI Design"
],

"Data Scientist": [
"Python",
"Statistics",
"Machine Learning",
"Pandas",
"NumPy",
"SQL",
"Data Visualization",
"Deep Learning"
],

"Data Analyst": [
"Excel",
"SQL",
"Python",
"Data Visualization",
"Statistics",
"Power BI",
"Tableau",
"Data Cleaning"
],

"Machine Learning Engineer": [
"Python",
"Machine Learning Algorithms",
"TensorFlow",
"PyTorch",
"Statistics",
"Data Processing",
"Model Deployment"
],

"AI Engineer": [
"Python",
"Machine Learning",
"Deep Learning",
"TensorFlow",
"PyTorch",
"NLP",
"Computer Vision"
],

"Cyber Security Analyst": [
"Networking",
"Linux",
"Security Monitoring",
"Threat Analysis",
"Firewalls",
"SIEM Tools",
"Incident Response"
],

"Ethical Hacker": [
"Networking",
"Linux",
"Penetration Testing",
"Vulnerability Assessment",
"Cryptography",
"Security Tools",
"Kali Linux"
],

"Cloud Engineer": [
"AWS",
"Azure",
"Google Cloud",
"Networking",
"Linux",
"Cloud Security",
"Virtualization"
],

"DevOps Engineer": [
"Linux",
"Docker",
"Kubernetes",
"CI/CD",
"Automation",
"Cloud Platforms",
"Scripting"
],

"Network Engineer": [
"Networking",
"TCP/IP",
"Routing",
"Switching",
"Firewalls",
"Network Security"
],

"System Administrator": [
"Linux",
"Windows Server",
"Networking",
"System Monitoring",
"Backup Systems",
"User Management"
],

"Blockchain Developer": [
"Solidity",
"Ethereum",
"Smart Contracts",
"Cryptography",
"Web3",
"JavaScript"
],

"IoT Engineer": [
"Embedded Systems",
"C Programming",
"Sensors",
"Microcontrollers",
"Networking",
"Cloud Integration"
],

"UI Designer": [
"Figma",
"Adobe XD",
"Wireframing",
"Prototyping",
"Color Theory",
"Typography"
],

"UX Designer": [
"User Research",
"Wireframing",
"Prototyping",
"Usability Testing",
"Interaction Design"
],

"Software Tester": [
"Manual Testing",
"Automation Testing",
"Selenium",
"Test Cases",
"Bug Tracking",
"Quality Assurance"
],

"QA Engineer": [
"Software Testing",
"Automation Tools",
"Test Planning",
"Performance Testing",
"Bug Tracking",
"Continuous Testing"
]

}