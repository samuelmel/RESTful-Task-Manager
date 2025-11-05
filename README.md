# 🚀 RESTful Task Manager

This project is a full-stack task management application (To-Do List) developed using Python and Flask for the backend, with data persistence in PostgreSQL, and a modern, light user interface built with pure HTML/CSS.

The application is structured following the RESTful standard to demonstrate the creation of a robust API, ready to be consumed by any frontend or service.

## ✨ Project Highlights

* **RESTful Backend:** Complete API (CRUD) using Python and the **Flask** micro-framework.
* **Persistence:** Uses **PostgreSQL** (via `Flask-SQLAlchemy`) for secure and scalable task storage.
* **Frontend:** Simple and responsive interface, developed with HTMLand styled with CSS.
* **Clean Structure:** Implements code organization using **Blueprints** and separates static logic (`/static`) and templates (`/templates`).

## 🛠️ Technologies Used

| Category | Technology | Project Usage |
| :--- | :--- | :--- |
| **Backend** | Python | Main programming language. |
| **Framework** | Flask | Micro-framework structure for the API. |
| **ORM** | Flask-SQLAlchemy | Object-Relational Mapping to interact with the DB. |
| **Database** | PostgreSQL | Relational database for data persistence. |
| **Frontend** | HTML |
| **Styling** | CSS | 

## ⚙️ How to Run the Project (Locally)

### Pre requisites

You will need to have the following installed on your machine:
1.  Python 3 (version 3.8+)
2.  `pip` (Python package manager)

### 1. Clone the Repository

```bash
git clone [https://github.com/samuelmel/RESTful-Task-Manager.git]
cd RESTful-Task-Manager
```

### 2. Configure the Virtual Environment
It is highly recommended to use a virtual environment to isolate dependencies.

```bash

# Creates the virtual environment
python -m venv venv

# Activates the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate
```

3. Install Dependencies
With the venv activated, install all packages listed in requirements.txt:

```bash

pip install -r requirements.txt
```

4. Configure Environment Variables (.env)
Create a file in the project root called .env. This file must contain the connection string for your PostgreSQL database.

.env Model:

# Replace the credentials and host with your own
SQLALCHEMY_DATABASE_URI="postgresql://USER:PASSWORD@HOST:PORT/DATABASENAME"

5. Start the Flask Application
The application is configured to start the API routes and create the database tables automatically.

```bash

# Defines the Flask startup file and debug mode
export FLASK_APP=app

# Runs the application
flask run
```
6. Access
Access the application in your browser, usually at:

➡️ http://127.0.0.1:5000/
