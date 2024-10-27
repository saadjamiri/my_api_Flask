# Flask User Management API & Web Application

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Phase 1: API REST](#phase-1-api-rest)
  - [Phase 2: Web Application](#phase-2-web-application)
- [Testing the API](#testing-the-api)
- [Future Enhancements](#future-enhancements)
- [Screenshots](#screenshots)
- [License](#license)
- [Author](#author)

## Introduction
This project demonstrates the creation of a simple Flask application with two main phases:

- **Phase 1**: Develop a basic REST API to manage users (add and retrieve users).
- **Phase 2**: Build a web interface that allows the user to add new users via a form and list existing users.

The project is useful for learning how to:
- Build REST APIs with Flask.
- Use HTTP methods like GET and POST.
- Test APIs with Postman or Insomnia.
- Integrate an HTML front-end with Flask.

## Project Structure 
/votre_projet
    /static
        my_first_app.png
        style.css
    /templates
        main.html
        index.html
        add_user.html
        list_users.html
    api.py
    README.md
    requirements.txt



## Requirements
- Python 3.x
- Flask
- Postman or Insomnia (for API testing)

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/saadjamiri/my_api_Flask.git
cd my_api_Flask
```
### Step  2 : Install the dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Flask app
```bash
python api.py
```


## Usage 

### Phase 1: API REST

In this phase, we will build a REST API that allows users to:

  GET a list of users at /users.
  POST new users to /users.
 
 **API Endpoints**

  GET /users: Returns the list of users in JSON format.
  POST /users: Adds a new user to the list (accepts a JSON body).

Example of a POST request body: 
{
    "first_name": "Charlie",
    "last_name": "Brown",
    "birth_date": "2000-01-01",
    "birth_city": "Paris"
}

### Phase 2: Web Application

In this phase, we will create a web interface to interact with the user data:

  A page to add a new user via a form (/add_user).
  A page to display all users (/list_users).

 **Routes**

  /add_user: Renders a form that allows users to add new entries.
 /list_users: Displays a list of all added users. 

 **Testing the API**
 You can test the API using Postman or Insomnia by following these steps:

**Step 1**: Run the Flask app

Start the server by running:
 python api.py
The application will run on http://localhost:5000

**Step 2**: Test the GET and POST routes

  GET /users: Retrieves a list of users. Example URL: http://localhost:5000/users

  POST /users: Adds a new user by sending a JSON payload. Example URL: http://localhost:5000/users

**Step 3**: Verify the results

After the POST request, use the GET /users route to verify that the user was added successfully.

**Future Enhancements**

Here are some features that could be added to improve the project:

  Add user validation (e.g., non-empty names).
  Implement user deletion and updating functionality.
  Store users in a database (e.g., SQLite, ) instead of in-memory.
  Add user authentication for the web interface and API.

**License**

This project is licensed under the MIT License. See the LICENSE file for more details.

**Author**

Developed by saadjamiri. For any questions, please contact saad1.jamiri@gamil.com.

