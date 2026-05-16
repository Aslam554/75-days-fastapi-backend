# FastAPI Backend Developer — Lecture 0 & 1 Notes

---

# What is FastAPI?

FastAPI is a modern Python web framework used for building fast and scalable APIs.

Built on:

* Starlette
* Pydantic

---

# Why FastAPI is Popular?

* Very fast performance
* Easy to learn
* Automatic API documentation
* Built-in data validation
* Async support
* Clean and modern syntax
* Production ready

---

# Key Features

* JSON REST APIs
* Swagger UI (`/docs`)
* ReDoc (`/redoc`)
* Pydantic validation
* Async & Await support
* File uploads
* JWT Authentication
* Background tasks
* Database integration
* HTML responses

---

# Project Setup Using UV

## Step 1 — Initialize Project

```bash
uv init project_name
```

Creates a new Python project.

---

## Step 2 — Move Into Project Folder

```bash
cd project_name
```

---

## Step 3 — Install FastAPI

```bash
uv add fastapi[standard]
```

Installs:

* FastAPI
* Uvicorn
* Standard dependencies

---

# Run FastAPI Server

```bash
uv run fastapi dev main.py
```

---

# Open API Docs

## Swagger Docs

```bash
http://127.0.0.1:8000/docs
```

Interactive API testing UI.

---

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

Clean API documentation.

---

# Creating FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()
```

## What is `app`?

* FastAPI instance
* Used to define routes/endpoints

---

# Creating Routes

```python
@app.get("/")
def home():
    return {"message": "Hello World"}
```

## Understanding

### `@app.get("/")`

* Route decorator
* Defines GET request endpoint

### `def home()`

* Function executed when route is called

---

# JSON Response

```python
return {"message": "Hello"}
```

FastAPI automatically converts Python dictionaries into JSON.

---

# Dummy Data Example

```python
posts = [
    {
        "id": 1,
        "author": "Aslam",
        "title": "FastAPI Basics"
    },
    {
        "id": 2,
        "author": "Rahul",
        "title": "Backend Development"
    }
]
```

Structure:

* List of dictionaries

---

# Returning Dummy Data

```python
@app.get("/api/posts")
def get_posts():
    return posts
```

FastAPI automatically returns JSON response.

---

# Reading Data from `data.txt`

## data.txt

```txt
[
  {
    "id": 1,
    "author": "Aslam",
    "title": "FastAPI Basics"
  }
]
```

---

## main.py

```python
import json

with open("data.txt", "r") as file:
    posts = json.load(file)
```

## Why `json.load()`?

Converts JSON text data into Python objects.

---

# HTML Response

By default FastAPI returns JSON.

To return HTML:

```python
from fastapi.responses import HTMLResponse
```

---

# HTML Example

```python
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <h1>Hello FastAPI</h1>
    """
```

---

# Why Use HTMLResponse?

Used for:

* webpages
* dashboards
* admin panels
* browser rendering

---

# Multiple Routes on Same Function

```python
@app.get("/")
@app.get("/posts")
def home():
    return {"message": "Hello"}
```

One function can handle multiple routes.

---

# Looping Through Posts in HTML

```python
@app.get("/posts", response_class=HTMLResponse)
def home():

    dt = ""

    for i in posts:
        dt += f"<h1>{i['title']}</h1>"

    return dt
```

---

# ASGI

## Full Form

```text
Asynchronous Server Gateway Interface
```

Modern interface between:

* web server
* FastAPI application

---

# Why ASGI?

* Handles multiple requests concurrently
* Better performance
* Supports async/await
* Used in scalable production apps

---

# ASGI Server

```bash
uvicorn
```

Runs FastAPI applications.

---

# Async Function

```python
async def home():
```

## Benefits

* Better concurrency
* Efficient request handling
* Improved scalability

---

# Hide HTML Routes from Docs

Use:

```python
include_in_schema=False
```

---

# Example

```python
from fastapi.responses import HTMLResponse

@app.get(
    "/",
    response_class=HTMLResponse,
    include_in_schema=False
)
def home():

    return "<h1>Hello FastAPI</h1>"
```

---

# Why Use `include_in_schema=False`?

Route will not appear in:

* `/docs`
* `/redoc`

Used for:

* HTML pages
* dashboards
* internal routes

Keeps API documentation clean.

---

# Testing APIs with CURL

```bash
curl -X GET "http://127.0.0.1:8000/api/posts"
```

Used for:

* API testing
* debugging
* terminal requests

---

# Core Concepts Covered Till Now

* FastAPI basics
* Routes
* JSON responses
* HTML responses
* Dummy data
* API documentation
* ASGI
* Async functions
* Swagger UI
* ReDoc
* Reading external data
* API testing

---

# Real World Use Cases

FastAPI is commonly used for:

* AI/ML backends
* REST APIs
* Authentication systems
* SaaS products
* Dashboards
* Real-time systems
* Startup backend infrastructure

---

# Key Takeaway

FastAPI is a fast, modern, and production-ready Python framework for building scalable backend APIs with automatic documentation, async support, and clean developer experience.
