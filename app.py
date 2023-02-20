from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "job_title": "Software Engineer",
        "location": "San Francisco",
        "salary": 120000
    },
    {
        "id": 2,
        "job_title": "Data Analyst",
        "location": "New York",
        # "salary": 80000
    },
    {
        "id": 3,
        "job_title": "Marketing Manager",
        "location": "Los Angeles",
        "salary": 100000
    },
    {
        "id": 4,
        "job_title": "Product Manager",
        "location": "Seattle",
        "salary": 130000
    },
    {
        "id": 5,
        "job_title": "UX Designer",
        "location": "Chicago",
        "salary": 90000
    },
    {
        "id": 6,
        "job_title": "Sales Representative",
        "location": "Dallas",
        "salary": 70000
    },
    {
        "id": 7,
        "job_title": "Human Resources Specialist",
        "location": "Atlanta",
        "salary": 85000
    },
    {
        "id": 8,
        "job_title": "Financial Analyst",
        "location": "Houston",
        "salary": 95000
    },
    {
        "id": 9,
        "job_title": "Project Manager",
        "location": "Boston",
        "salary": 110000
    },
    {
        "id": 10,
        "job_title": "Customer Service Representative",
        "location": "Miami",
        "salary": 60000
    }
]


@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)
