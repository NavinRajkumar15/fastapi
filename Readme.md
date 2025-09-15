# FastAPI Project – Customer Management

A simple **FastAPI** application with a local SQLite database.  
Currently supports a `User` model inside a `customers` database.  
You can expand with more models later.

---

## 🚀 Features
- FastAPI app with SQLAlchemy ORM  
- Local SQLite database (`customers.db`)  
- User model with:
  - `id` (auto-increment primary key)  
  - `name`  
  - `email`  
- Unit tests using **pytest**  

---

## 📂 Project Structure
```plaintext
Python_Fast_API/
│── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI entrypoint
│   ├── models.py         # SQLAlchemy models
│   ├── db.py             # DB engine + session
│   ├── crud.py           # Database operations
│   └── schemas.py        # Pydantic schemas
│
│── tests/
│   ├── __init__.py
│   ├── conftest.py       # Pytest fixtures (test DB, session)
│   └── test_users.py     # Example unit tests
│
│── requirements.txt
│── README.md

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Python_Fast_API.git
cd Python_Fast_API

### 2️⃣ Create a virtual environment
```bash
python -m venv fastEnv

### 3️⃣ Activate the virtual environment
On Windows (PowerShell):
fastEnv\Scripts\activate

### 4️⃣ Install dependencies
pip install -r requirements.txt

### ▶️ Running the App
uvicorn app.main:app --reload

Now open your browser:

API Docs → http://127.0.0.1:8000/docs

OpenAPI JSON → http://127.0.0.1:8000/openapi.json