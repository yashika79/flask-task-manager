# 📝 Flask To-Do App

A simple task management web application built using **Python, Flask, Flask-SQLAlchemy, and SQLite**. Users can register, log in, and manage their personal tasks.

## ✨ Features

- User registration and login
- Password hashing using Werkzeug
- Session-based authentication
- Create, view, edit, and delete tasks
- Track task status: Pending, In Progress, and Done
- Assign planned dates to tasks
- User-specific task access
- Clear all tasks belonging to the logged-in user

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite, Flask-SQLAlchemy
- **Forms & Security:** Flask-WTF, WTForms, Werkzeug
- **Frontend:** HTML, CSS, Jinja2
- **Migrations:** Flask-Migrate, Alembic

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd To-Do
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python run.py
```

Open **http://127.0.0.1:5000/** in your browser.

## 📚 What I Learnt

- Flask routing and Blueprints
- CRUD operations with SQLAlchemy
- User authentication and session management
- Password hashing
- Database migrations
- User-specific data access and authorization
- Dynamic HTML rendering with Jinja2

## 🔮 Future Improvements

- Automated testing
- Task priorities and categories
- Search and filtering
- Improved validation and error handling
- Application deployment

## 👩‍💻 Author

**Yashika Varshney**
