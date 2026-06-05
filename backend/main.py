from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import text

from backend.database import engine
from backend.sql_guard import is_safe_sql
from backend.openai_service import generate_sql

app = FastAPI(title="AskSQL API")


class SQLRequest(BaseModel):
    sql: str


class AskRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AskSQL API Running"}


@app.get("/customers")
def get_customers():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM customers"))
        rows = [dict(row._mapping) for row in result]

    return rows


@app.post("/run-sql")
def run_sql(request: SQLRequest):
    if not is_safe_sql(request.sql):
        return {"error": "Only safe SELECT queries are allowed."}

    with engine.connect() as conn:
        result = conn.execute(text(request.sql))
        rows = [dict(row._mapping) for row in result]

    return {
        "sql": request.sql,
        "rows": rows
    }


@app.post("/ask")
def ask_question(request: AskRequest):
    try:
        generated_sql = generate_sql(request.question)

        if not is_safe_sql(generated_sql):
            return {
                "question": request.question,
                "generated_sql": generated_sql,
                "error": "Generated SQL was blocked for safety."
            }

        with engine.connect() as conn:
            result = conn.execute(text(generated_sql))
            rows = [dict(row._mapping) for row in result]

        return {
            "question": request.question,
            "generated_sql": generated_sql,
            "rows": rows
        }

    except Exception as e:
        return {
            "question": request.question,
            "error": str(e)
        }