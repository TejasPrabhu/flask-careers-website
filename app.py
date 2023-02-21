from flask import Flask, render_template, jsonify, request
from database import save_application_data, load_jobs_from_db, load_job_from_db


app = Flask(__name__)


@app.route('/')
def home():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
    jobs = load_job_from_db(id)
    if not jobs:
        return 'Not Found', 404
    return render_template('jobpage.html', job=jobs)


@app.route('/job/<id>/apply', methods=['post'])
def apply_to_job(id):
    data = request.form
    save_application_data(job_id=id, application=data)
    return render_template('application_submitted.html', application=data)


# JOBS = [
#     {
#         "id": 1,
#         "job_title": "Software Engineer",
#         "location": "San Francisco",
#         "salary": 120000
#     },
#     {
#         "id": 2,
#         "job_title": "Data Analyst",
#         "location": "New York",
#         # "salary": 80000
#     },
#     {
#         "id": 3,
#         "job_title": "Marketing Manager",
#         "location": "Los Angeles",
#         "salary": 100000
#     },
#     {
#         "id": 4,
#         "job_title": "Product Manager",
#         "location": "Seattle",
#         "salary": 130000
#     },
#     {
#         "id": 5,
#         "job_title": "UX Designer",
#         "location": "Chicago",
#         "salary": 90000
#     },
#     {
#         "id": 6,
#         "job_title": "Sales Representative",
#         "location": "Dallas",
#         "salary": 70000
#     },
#     {
#         "id": 7,
#         "job_title": "Human Resources Specialist",
#         "location": "Atlanta",
#         "salary": 85000
#     },
#     {
#         "id": 8,
#         "job_title": "Financial Analyst",
#         "location": "Houston",
#         "salary": 95000
#     },
#     {
#         "id": 9,
#         "job_title": "Project Manager",
#         "location": "Boston",
#         "salary": 110000
#     },
#     {
#         "id": 10,
#         "job_title": "Customer Service Representative",
#         "location": "Miami",
#         "salary": 60000
#     }
# ]
