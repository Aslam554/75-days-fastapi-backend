# Student Management API — FastAPI Beginner Project

## Overview

A beginner-friendly FastAPI project built while learning backend development fundamentals.

This project demonstrates:

* FastAPI routing
* HTML responses
* Dynamic path parameters
* Jinja2 templates
* Dummy student data handling
* API development basics

---

# Features

* Home page using Jinja2 templates
* Get all student details
* Get single student by ID
* Dynamic API routes
* HTML rendering with FastAPI
* External dummy data file

---

# Tech Stack

* Python
* FastAPI
* Jinja2
* HTML

---

# Project Structure

```bash id="3m8v1q"
project/
│
├── main.py
├── students.py
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# Installation

## Clone Repository

```bash id="9q2m5x"
git clone <repo-link>
```

---

## Move Into Project

```bash id="5v1m8q"
cd project-name
```

---

## Install Dependencies

```bash id="2m7q4x"
uv add fastapi[standard]
uv add jinja2
```

---

# Run Server

```bash id="7x1m5q"
uv run fastapi dev main.py
```

---

# API Routes

## Home Route

```bash id="1q8m4v"
/
```

Renders HTML homepage using Jinja2 templates.

---

## Get All Students

```bash id="4m7q2x"
/api/students
```

Returns all student details.

---

## Get Single Student

```bash id="8v2m5q"
/api/students/{id}
```

Example:

```bash id="3q1m8v"
/api/students/1
```

Returns student details by ID.

---

# Concepts Learned

* FastAPI basics
* Routes and endpoints
* HTMLResponse
* Dynamic path parameters
* Loops and conditions
* Jinja2 templates
* Rendering HTML pages
* Dummy API development

---

# Future Improvements

* Add CRUD operations
* Connect PostgreSQL database
* Add authentication
* Add CSS styling
* Convert to REST API responses
* Deploy project online

---

# Learning Goal

This project is part of:

> 75 Days of becoming a FastAPI Backend Developer and landing a startup job.
