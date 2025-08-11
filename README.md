# Simple User Management API

This is a basic RESTful API for managing a list of users. It's built with Node.js and Express.

## Getting Started

### Prerequisites

*   [Node.js](https://nodejs.org/) installed on your machine.

### Installation

1.  Clone the repository (if you haven't already).
2.  Navigate to the project directory in your terminal.
3.  Install the required npm packages:
    ```bash
    npm install
    ```

### Running the API Server

To start the server, run the following command in the project's root directory:

```bash
npm start
```

The server will start and listen on `http://localhost:3050`.

## API Endpoints

You can interact with the API using the provided `index.html` file in your browser or by using a tool like `curl`.

Below are examples using `curl` in a **PowerShell** terminal.

### 1. Create a New User

Send a `POST` request to `/users` to add a new user.

```powershell
curl -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"name":"New User","email":"new.user@example.com"}' -Uri http://localhost:3050/users
```

### 2. Get a List of All Users

Send a `GET` request to `/users` to retrieve all users.

```powershell
curl http://localhost:3050/users
```

### 3. Update a User

Send a `PUT` request to `/users/{id}` to update a specific user. Replace `{id}` with the user's actual ID.

```powershell
# Example for user with ID 1
curl -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"name":"Updated Name","email":"updated.email@example.com"}' -Uri http://localhost:3050/users/1
```

### 4. Delete a User

Send a `DELETE` request to `/users/{id}` to remove a specific user.

```powershell
# Example for user with ID 1
curl -Method DELETE -Uri http://localhost:3050/users/1
```
