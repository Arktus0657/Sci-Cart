# FastAPI Product Management API

## Overview
This project is a **FastAPI-based REST API** that performs **CRUD operations (Create, Read, Update, Delete)** for product management using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

The API allows you to:
- View all products
- View a product by ID
- Add a new product
- Update an existing product
- Delete a product

The database is automatically initialized with sample product data when the server starts.

---

## Tech Stack
- **FastAPI** – Backend framework
- **PostgreSQL** – Database
- **SQLAlchemy** – ORM
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server

---

## Project Structure
```
├── db_config.py # Database connection configuration
├── db_models.py # SQLAlchemy database models
├── models.py # Pydantic models (request/response schemas)
├── main.py # FastAPI application and API routes
├── README.md
├── .gitignore
└── fastapioneshot/ # Virtual environment
```
---
## Database Configuration
Update the PostgreSQL connection URL in `db_config.py` if needed:

```python
db_url = "postgresql://postgres:1234@localhost:5432/fastapitestdb"
```
Make sure PostgreSQL is running and the database fastapitestdb exists.
---
## Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```
### 2. Create virtual environment
```bash
python -m venv fastapioneshot
```
### 3. Activate virtual environment
**Windows:**
```bash
fastapioneshot\Scripts\activate
```
**Linux/Mac:**
```bash
source fastapioneshot/bin/activate
```
### 4. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2
```
### 5. Run the server
```bash
uvicorn main:app --reload
```
**Server will start at:**
```
http://127.0.0.1:8000
```
**Swagger UI:**
```
http://127.0.0.1:8000/docs
```
## API Endpoints
| Method         | Endpoint                                                       | Description                                                       |
| -------------- | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| GET            | /                                                              | Welcome message                                                   |
| GET            | /products                                                      | Get all products                                                  |
| GET            | /products/{id}                                                 | Get product by ID                                                 |
| POST           | /products                                                      | Add new product                                                   |
| PUT            | /products/{id}                                                 | Update product                                                    |
| DELETE         | /products?id=                                                  | Delete product                                                    |

