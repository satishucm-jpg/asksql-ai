from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://asksql_user:asksql_pass@localhost:3306/asksql_db"
)

engine = create_engine(DATABASE_URL)