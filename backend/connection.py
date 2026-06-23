import psycopg2
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus

load_dotenv()

def get_connection():
    conn=psycopg2.connect(
        host=os.environ.getenv("DB_HOST"),
        port=os.environ.getenv("DB_PORT"),
        dbname=os.environ.getenv("DB_NAME"),
        user=os.environ.getenv("DB_USER"),
        password=os.environ.getenv("DB_PASSWORD")
    )
    return conn


def get_engine():
    password = quote_plus(os.environ.getenv('DB_PASSWORD'))
    return create_engine(
        f"postgresql://{os.environ.getenv('DB_USER')}:{password}@{os.environ.getenv('DB_HOST')}:{os.environ.getenv('DB_PORT')}/{os.environ.getenv('DB_NAME')}"
    )


if __name__=="__main__":
    try:
        conn = get_connection()
        print("✅ Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print(f"❌ Connection failed: {e}")