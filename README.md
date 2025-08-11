# Simple User Management API

This is a basic RESTful API for managing a list of users. It's built with Node.js, Express, and PostgreSQL.

## Getting Started

### Prerequisites

*   [Node.js](https://nodejs.org/) installed on your machine.
*   [PostgreSQL](https://www.postgresql.org/) installed and running.

### Database Setup

1.  Connect to your PostgreSQL instance using `psql` or another client.
2.  Create the database for this project:
    ```sql
    CREATE DATABASE api;
    ```
3.  Connect to the new `api` database:
    ```sql
    \c api
    ```
4.  Create the `users` table:
    ```sql
    CREATE TABLE users (
      ID SERIAL PRIMARY KEY,
      name VARCHAR(30),
      email VARCHAR(30)
    );
    ```
5.  Update the database connection details in `db.js` with your PostgreSQL username and password.

### Installation

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Install the required npm packages:
    ```bash
    npm install
    ```

### Running the API Server

To start the server, run the following command:

```bash
npm start
```

The server will start and listen on `http://localhost:3050`.

## API Endpoints

You can interact with the API using a tool like `curl`.

### `curl` Commands for Windows CMD

#### Create a User
```powershell
curl.exe -X POST -H "Content-Type: application/json" -d "{\\"name\\":\\"John Doe\\",\\"email\\":\\"john.doe@example.com\\"}" http://localhost:3050/users
```

#### Get All Users
```powershell
curl.exe http://localhost:3050/users
```

#### Update a User
*Replace `1` with the user's ID.*
```powershell
curl.exe -X PUT -H "Content-Type: application/json" -d "{\\"name\\":\\"Johnathan Doe\\",\\"email\\":\\"johnathan.d@example.com\\"}" http://localhost:3050/users/1
```

#### Delete a User
*Replace `1` with the user's ID.*
```powershell
curl.exe -X DELETE http://localhost:3050/users/1
```

### `curl` Commands for PowerShell

#### Create a User
```powershell
Invoke-WebRequest -Uri http://localhost:3050/users -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"name":"New User","email":"new.user@example.com"}'
```

#### Get All Users
```powershell
Invoke-WebRequest -Uri http://localhost:3050/users
```

#### Update a User
*Replace `1` with the user's ID.*
```powershell
Invoke-WebRequest -Uri http://localhost:3050/users/1 -Method PUT -Headers @{"Content-Type"="application/json"} -Body '{"name":"Updated Name","email":"updated.email@example.com"}'
```

#### Delete a User
*Replace `1` with the user's ID.*
```powershell
Invoke-WebRequest -Uri http://localhost:3050/users/1 -Method DELETE
```

