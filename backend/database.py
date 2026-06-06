import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://asksql_user:asksql_pass@localhost:3306/asksql_db"
)

engine = create_engine(DATABASE_URL)