# Expense Management System

This project is an advanced Expense Management System that consists of a **Streamlit** frontend application and a **FastAPI** backend server. It helps users efficiently track and analyze expenses with interactive visualizations and a user-friendly interface.

---

## 🚀 Features

- **Expense Tracking**: Add, update, and delete expenses effortlessly.
- **Category-Based Analytics**: View expenses categorized for better insights.
- **Monthly Analysis**: Get a breakdown of expenses by month.
- **FastAPI Backend**: Ensures a fast, scalable, and efficient API.
- **Streamlit UI**: Provides an intuitive interface for users.
- **Automated Tests**: Covers both frontend and backend components.
- **Easy Deployment**: Can be hosted on cloud platforms.

---

## 📁 Project Structure

- **`frontend/`** - Contains the Streamlit application code.
- **`backend/`** - Houses the FastAPI backend server.
- **`tests/`** - Includes test cases for both frontend and backend.
- **`requirements.txt`** - Lists all necessary dependencies.
- **`README.md`** - Documentation and setup guide.

---

## 📷 Sample Screenshots

### ➕ Add/Update Expenses
![Add Update](https://github.com/user-attachments/assets/4a7560cf-fea8-467a-a985-ea6c299177f6)

### 📊 Analytics by Category
![Analytics Categories](https://github.com/user-attachments/assets/b82dfdb7-445d-43bf-8a25-31320f4ff5a4)

### 📅 Analytics by Month
![Analytics Month](https://github.com/user-attachments/assets/0b5887a1-4f65-4270-8238-ca7c6211cb26)

---

## 🛠 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/subhadeep414/Expense-Management-System.git
cd Expense-Management-System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Backend Server
```bash
cd backend
uvicorn server:app --reload
```

### 4️⃣ Start the Streamlit Frontend Application
```bash
streamlit run frontend/app.py
```

---

## 📡 API Documentation
Once the backend is running, you can access the API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📜 License
This project is licensed under the **MIT License**.

---
