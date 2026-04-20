# FastAPI Learning Project

A simple, well-documented FastAPI project designed for learning the basics of building RESTful APIs with Python. This project covers various endpoint types, including GET/POST requests and query/body parameters.

## 🚀 Features

- **Root Endpoint**: Basic "Hello World" response.
- **About Endpoint**: Metadata about the application.
- **Query Parameters**: Dynamic greeting and mathematical operations via URL parameters.
- **POST Requests**: Structured data handling using Pydantic schemas.
- **Automatic Documentation**: Built-in Swagger UI and ReDoc support.

## 🛠️ Prerequisites

- Python 3.7+
- pip (Python package installer)

## 📥 Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd fastapi_project
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running the Application

Start the development server using `uvicorn`:

```bash
uvicorn main:app --reload
```

- `main`: The filename (`main.py`).
- `app`: The FastAPI instance created inside `main.py`.
- `--reload`: Automatically restarts the server when code changes.

The API will be available at: **`http://127.0.0.1:8000`**

## 📖 API Documentation

FastAPI provides interactive documentation out of the box:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📡 Endpoints Summary

| Method | Endpoint | Description | Example |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | Returns a simple hello world message. | `http://localhost:8000/` |
| **GET** | `/about` | Returns application metadata. | `http://localhost:8000/about` |
| **GET** | `/greet` | Greets a user by name via query param. | `http://localhost:8000/greet?name=Vaibhavi` |
| **GET** | `/add` | Adds two integers provided as query params. | `http://localhost:8000/add?a=10&b=5` |
| **POST** | `/greet` | Greets a user using data from a JSON body. | Body: `{"name": "Vaibhavi", "age": 22}` |

## 🏗️ Project Structure

```text
fastapi_project/
├── main.py          # Application entry point & endpoint definitions
├── requirements.txt # Project dependencies (fastapi, uvicorn)
└── .vscode/         # Local editor configuration
```

## 📝 License

This project is open-source and available for learning purposes.
