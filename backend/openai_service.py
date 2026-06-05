import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_sql(question: str) -> str:
    schema = """
    customers(customer_id, customer_name, city, signup_date)

    products(product_id, product_name, category, price)

    orders(order_id, customer_id, product_id, order_date, quantity, total_amount)
    """

    prompt = f"""
    You are an expert MySQL assistant.

    Convert the user question into a safe MySQL SELECT query.

    Rules:
    - Return ONLY SQL.
    - No markdown.
    - No explanation.
    - Only SELECT statements.

    Schema:
    {schema}

    User Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql