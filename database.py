import os
from sqlalchemy import create_engine, text

database = 'caimcareers'
username = 't4u2amuzklhwwsm3n8kd'
host = 'us-east.connect.psdb.cloud'
password = 'pscale_pw_PcD2C9Ygj3Q6ScuvycI7eGVY0h2qDfiuRk6ZybawkIB'

# DB_CONNECTION_STRING = os.environ('DB_CONNECTION_STRING')"mysql+pymysql://t4u2amuzklhwwsm3n8kd:pscale_pw_PcD2C9Ygj3Q6ScuvycI7eGVY0h2qDfiuRk6ZybawkIB@us-east.connect.psdb.cloud/caimcareers?charset=utf8mb4"
DB_CONNECTION_STRING = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb4",
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })


def load_jobs_from_db():
    with engine.connect() as conn:
        results = conn.execute(text("select * from jobs"))
        jobs = []
        for row in results:
            jobs.append(dict(row._mapping))
    return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        results = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        rows = results.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._mapping)


def save_application_data(job_id, application):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        conn.execute(query, {"job_id": job_id, "full_name": application['full_name'], "email": application['email'], "linkedin_url": application[
                     'linkedin'], "education": application['education'], "work_experience": application['work_ex'], "resume_url": application['resume_url']})
