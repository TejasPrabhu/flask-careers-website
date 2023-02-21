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
