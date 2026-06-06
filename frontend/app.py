import streamlit as st
import requests
import pandas as pd

API_URL = "API_URL = "https://asksql-ai.onrender.com/ask""

st.set_page_config(page_title="AskSQL AI", page_icon="🧠", layout="wide")

st.title("AskSQL AI")
st.write("Ask questions in English and get SQL-powered answers from MySQL.")

question = st.text_input("Ask a question:", placeholder="Example: Show customers from Chicago")

if st.button("AskSQL"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating SQL and querying MySQL..."):
            response = requests.post(API_URL, json={"question": question})

        data = response.json()

        if "error" in data:
            st.error(data["error"])
            if "generated_sql" in data:
                st.code(data["generated_sql"], language="sql")
        else:
            st.subheader("Generated SQL")
            st.code(data["generated_sql"], language="sql")

            st.subheader("Results")
            rows = data["rows"]

            if rows:
                df = pd.DataFrame(rows)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("No results found.")