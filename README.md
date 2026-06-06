# 🧠 AskSQL AI

AskSQL AI is an AI-powered Natural Language to SQL application that allows users to query a database using plain English.

Instead of writing SQL manually, users can ask questions like:

> Show customers from Chicago

and the application automatically:

1. Converts the question into SQL using OpenAI GPT
2. Validates the SQL for safety
3. Executes the query against MySQL
4. Returns the results in a user-friendly interface

---

# 🚀 Live Demo

### Frontend (Streamlit)

https://asksql-ai-udauhpswczi2mwggh4jm7g.streamlit.app/

### Backend API (Render)

https://asksql-ai.onrender.com/docs

### GitHub Repository

https://github.com/satishucm-jpg/asksql-ai

---

# 📸 Project Demo

## Home Page

Home Page

---

## Natural Language to SQL Demo

User asks:

Show customers from Chicago

Generated SQL:

sql SELECT * FROM customers WHERE city = 'Chicago'; 

Results are automatically returned from MySQL.

NL to SQL Demo

---

## Customer Query Results

Customers Query

---

## Product Query Results

Products Query

---

## API Documentation

FastAPI Swagger documentation.

API Docs

---

## MySQL Running in Docker

Local MySQL database running inside Docker.

Docker MySQL

---

# 📌 Features

- Natural Language to SQL using OpenAI GPT
- FastAPI backend
- MySQL database integration
- SQL query validation and safety checks
- Interactive Swagger API documentation
- Streamlit frontend
- Railway cloud database
- Render deployment
- End-to-end AI workflow

---

# 🏗️ Architecture

text User   │   ▼ Streamlit Frontend   │   ▼ FastAPI Backend   │   ▼ OpenAI GPT   │   ▼ SQL Validation Layer   │   ▼ MySQL Database (Railway) 

---

# 🛠️ Tech Stack

### Frontend
- Streamlit
- Pandas

### Backend
- FastAPI
- Uvicorn
- SQLAlchemy

### Database
- MySQL
- Railway

### AI
- OpenAI GPT

### Deployment
- Streamlit Cloud
- Render
- Railway

### Other Tools
- Docker
- GitHub

---

# 📂 Project Structure

text asksql-ai/ │ ├── backend/ │   ├── main.py │   ├── database.py │   ├── openai_service.py │   ├── sql_guard.py │ ├── frontend/ │   ├── app.py │ ├── sql/ │   └── sample_data.sql │ ├── screenshots/ │   ├── home-page.png │   ├── nl-to-sql-demo.png │   ├── customers-query.png │   ├── products-query.png │   ├── api-docs.png │   └── docker-mysql.png │ ├── docker-compose.yml ├── requirements.txt ├── start.sh └── README.md 

---

# 💡 Example Queries

text Show customers from Chicago 

text Show all products 

text Show all orders 

text Show customer names and cities 

---

# 🔒 SQL Safety

AskSQL AI includes a SQL validation layer that prevents execution of unsafe statements.

Allowed:

sql SELECT * FROM customers; 

Blocked:

sql DROP TABLE customers; 

sql DELETE FROM customers; 

sql TRUNCATE TABLE customers; 

sql ALTER TABLE customers; 

This ensures generated SQL remains read-only and safe.

---

# ⚙️ Local Setup

## Clone Repository

bash git clone https://github.com/satishucm-jpg/asksql-ai.git  cd asksql-ai 

## Install Dependencies

bash pip install -r requirements.txt 

## Start MySQL

bash docker compose up -d 

## Load Sample Data

bash docker exec -i asksql-mysql mysql -u asksql_user -pasksql_pass asksql_db < sql/sample_data.sql 

## Run Backend

bash uvicorn backend.main:app --reload 

## Run Frontend

bash streamlit run frontend/app.py 

---

# 📈 Future Enhancements

- Query history
- Data visualizations and charts
- CSV upload support
- Multiple database support (PostgreSQL, Snowflake)
- User authentication
- Saved dashboards
- Business insight generation
- AI-powered analytics assistant

---

# 👨‍💻 Author

Satish Reddy Mule

GitHub:  
https://github.com/satishucm-jpg

LinkedIn:  
Add your LinkedIn profile URL

---

# ⭐ Support

If you found this project useful, please consider giving it a star ⭐ on Git
