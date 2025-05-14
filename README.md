# 🧼 Simple SOAP CRUD API using Flask, Spyne & MySQL

This project demonstrates a **simple SOAP-based API built using Flask and Spyne**, with **MySQL as the backend database**.

It provides the following **CRUD operations** for managing users:
- Get User by Name
- Insert New User
- Update User Info
- Delete User

---

## 📁 Project Structure

```
code/
├── app.py                    # Flask application entry point
├── config/                   # Database configuration (database.py)
├── services/                 # Separate SOAP service files
├── base/                     # Common constants
├── schema/                   # SQL script for users table
├── example/                  # Sample SOAP request and response XML files
└── requirements.txt
```

---

## 🛠 Tech Stack

- Python 3.9
- Flask
- Spyne (SOAP)
- MySQL
- Postman / SOAP UI for testing

---

## 🚀 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/sample-soap-crud.git
cd sample-soap-crud/code
```

2. **Create and activate virtual environment (Python 3.9 only)**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup MySQL Database**
- Create a database (e.g., `sample_soap_db`).
- Execute the SQL script inside `schema/users.sql` to create the `users` table.

5. **Configure database connection**
- Rename `env_example` to `.env`
- Update your database credentials.

6. **Run the Application**
```bash
python app.py
```

---

## 🌐 SOAP Endpoint

- WSDL URL:  
  `http://localhost:5000/soap/?wsdl`

---

## 🧪 Testing the API

You can test the API using:
- **SOAP UI** (Recommended)
- **Postman** (Ensure "SOAP Request" plugin is used or use raw XML)

Sample request and response XML files are available inside the `example/` folder.

---

## 💾 Available Services

| Service Name            | Description       |
|-------------------------|-------------------|
| GetUserService           | Get user by name  |
| InsertUserService        | Add new user      |
| UpdateUserService        | Update user data  |
| DeleteUserService        | Delete user by ID |

---

## 📄 Author
- Created for learning purpose by Raghav Garg