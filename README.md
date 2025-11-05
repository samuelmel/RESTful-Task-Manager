🚀 RESTful Task Manager

This project is a full-stack task management application (To-Do List) developed using Python and Flask for the backend, with data persistence in PostgreSQL, and a modern, light user interface built with pure HTML/CSS.

The application is structured following the RESTful standard to demonstrate the creation of a robust API, ready to be consumed by any frontend or service.

✨ Project Highlights

RESTful Backend: Complete API (CRUD) using Python and the Flask micro-framework.

Persistence: Uses PostgreSQL (via Flask-SQLAlchemy) for secure and scalable task storage.

Frontend SPA: Simple and responsive interface, developed with HTML and styled with CSS.

Clean Structure: Implements code organization using Blueprints and separates static logic (/static) and templates (/templates).

🛠️ Technologies Used

Category

Technology

Project Usage

Backend

Python 3

Main programming language.

Framework

Flask

Micro-framework structure for the API.

ORM

Flask-SQLAlchemy

Object-Relational Mapping to interact with the DB.

Database

PostgreSQL

Relational database for data persistence.

Frontend

HTML, JavaScript

User interface and API consumption logic.

Styling

Tailwind CSS

Utility-first framework for modern, responsive design.

⚙️ How to Run the Project (Locally)

Prerequisites

You will need to have the following installed on your machine:

Python 3 (version 3.8+)

pip (Python package manager)

1. Clone the Repository

git clone [https://github.com/samuelmel/RESTful-Task-Manager.git](https://github.com/samuelmel/RESTful-Task-Manager.git)
cd RESTful-Task-Manager


2. Configure the Virtual Environment

It is highly recommended to use a virtual environment to isolate dependencies.

# Creates the virtual environment
python -m venv venv

# Activates the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1


3. Install Dependencies

With the venv activated, install all packages listed in requirements.txt:

pip install -r requirements.txt


4. Configure Environment Variables (.env)

Create a file in the project root called .env. This file must contain the connection string for your PostgreSQL database.

.env Model:

# Replace the credentials and host with your own
SQLALCHEMY_DATABASE_URI="postgresql://USER:PASSWORD@HOST:PORT/DATABASENAME" 


5. Start the Flask Application

The application is configured to start the API routes and create the database tables automatically.

# Defines the Flask startup file and debug mode
export FLASK_APP=app

# Runs the application
flask run


6. Access

Access the application in your browser, usually at:

➡️ https://www.google.com/search?q=http://127.0.0.1:5000/

💻 API Routes (Endpoints)

The API exposes the following routes:

Method

Endpoint

Description

Request Body

GET

/tasks

Lists all tasks.

(None)

POST

/tasks

Creates a new task.

{"title": "...", "description": "..."}

GET

/tasks/<id>

Fetches a specific task by ID.

(None)

PUT

/tasks/<id>

Updates the title, description, or status.

{"title": "...", "status": true}

DELETE

/tasks/<id>

Deletes a task.

(None)

GET

/

User interface route (HTML).

(None)

🤝 Contributions

Feel free to open issues or submit pull requests for improvements.
