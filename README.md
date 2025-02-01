# Contact App Backend

This is the backend for the Contact App, built with Flask. It provides APIs to manage users, contacts, and favorites.

## Features

- Manage users (create, read, update, delete)
- Manage contacts (create, read, update, delete)
- Manage favorite contacts (create, read, delete)

## Requirements

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-CORS

## Getting Started

### Installation

1. Clone the repository:

   ```sh
   git clone <git@github.com:Stephanieest/contact-app-backend.git>
   cd backend
Create and activate a virtual environment:

sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

sh
pip install -r requirements.txt
Database Setup
Initialize the database:

sh
flask db init
Create an initial migration:

sh
flask db migrate -m "Initial migration."
Apply the migration:

sh
flask db upgrade
Running the App
Start the Flask app:

sh
python app.py
The app will be running at http://127.0.0.1:5000.

API Endpoints
Users

GET /users - Get all users
POST /users - Create a new user
PUT /users/<id> - Update a user
DELETE /users/<id> - Delete a user
Contacts

GET /contacts - Get all contacts
POST /contacts - Create a new contact
PUT /contacts/<id> - Update a contact
DELETE /contacts/<id> - Delete a contact
Favorites

GET /favorites - Get all favorite contacts
POST /favorites - Add a contact to favorites
DELETE /favorites/<id> - Remove a contact from favorites
License
This project is licensed under the MIT License.