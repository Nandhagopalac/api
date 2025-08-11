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

---
# Complete API Documentation Guide for Beginners

## What is an API? (Simple Explanation)

Think of an API (Application Programming Interface) like a waiter in a restaurant:
- **You** (the customer) want something from the kitchen
- **The waiter** (the API) takes your order to the kitchen
- **The kitchen** (the server/database) prepares your food
- **The waiter** brings your food back to you

In technical terms: An API lets different software applications talk to each other and share information.

## Real-World Example
When you use a weather app on your phone:
1. The app asks a weather API: "What's the weather in New York?"
2. The API checks with weather databases
3. The API returns: "72°F, sunny, light breeze"
4. Your app displays this information nicely

---

# API Documentation Template

## 1. Getting Started

### What You'll Need
- **API Key**: A special password that identifies you (like a library card)
- **Base URL**: The main web address for our API
- **HTTP Client**: A tool to send requests (like Postman, or code)

### Quick Setup
1. Sign up for an account at [your-website.com]
2. Get your API key from your dashboard
3. Start making requests to: `https://api.yourservice.com`

---

## 2. Authentication (How to Prove You're Allowed)

### API Key Method (Recommended for beginners)
Add your API key to every request in the header:

```
Authorization: Bearer YOUR_API_KEY_HERE
```

**Example:**
```bash
curl -H "Authorization: Bearer abc123xyz789" https://api.yourservice.com/users
```

---

## 3. Making Your First Request

### Understanding HTTP Methods (Think of them as actions)
- **GET**: "Give me information" (like reading a book)
- **POST**: "Create something new" (like writing a new page)
- **PUT**: "Update/replace something" (like rewriting a whole page)
- **DELETE**: "Remove something" (like tearing out a page)

### Basic Request Structure
Every API request has:
1. **Method**: What action you want (GET, POST, etc.)
2. **URL**: Where to send the request
3. **Headers**: Extra information (like your API key)
4. **Body**: Data you're sending (for POST/PUT requests)

---

## 4. Sample API: User Management System

Let's create a simple user management API as an example.

### Base URL
```
https://api.yourservice.com/v1
```

### Available Endpoints

#### Get All Users
**What it does**: Gets a list of all users
```http
GET /users
```

**Response Example:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2024-01-15"
    },
    {
      "id": 2,
      "name": "Jane Smith", 
      "email": "jane@example.com",
      "created_at": "2024-01-16"
    }
  ]
}
```

#### Get One User
**What it does**: Gets details about a specific user
```http
GET /users/{user_id}
```

**Example Request:**
```http
GET /users/1
```

**Response Example:**
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-555-0123",
    "created_at": "2024-01-15",
    "last_login": "2024-03-10"
  }
}
```

#### Create New User
**What it does**: Adds a new user to the system
```http
POST /users
```

**Required Information:**
```json
{
  "name": "User's full name",
  "email": "user@example.com",
  "phone": "+1-555-0123"
}
```

**Example Request:**
```bash
curl -X POST https://api.yourservice.com/v1/users \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "phone": "+1-555-0199"
  }'
```

**Success Response:**
```json
{
  "status": "success",
  "message": "User created successfully",
  "data": {
    "id": 3,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "phone": "+1-555-0199",
    "created_at": "2024-03-10"
  }
}
```

#### Update User
**What it does**: Changes information about an existing user
```http
PUT /users/{user_id}
```

**Example Request:**
```bash
curl -X PUT https://api.yourservice.com/v1/users/3 \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Johnson-Smith",
    "phone": "+1-555-0200"
  }'
```

#### Delete User
**What it does**: Removes a user from the system
```http
DELETE /users/{user_id}
```

**Example Request:**
```bash
curl -X DELETE https://api.yourservice.com/v1/users/3 \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Success Response:**
```json
{
  "status": "success",
  "message": "User deleted successfully"
}
```

---

## 5. Understanding Responses

### HTTP Status Codes (What they mean)
- **200 OK**: Everything worked perfectly
- **201 Created**: New item was created successfully
- **400 Bad Request**: You sent incorrect information
- **401 Unauthorized**: Your API key is missing/invalid
- **404 Not Found**: The item you're looking for doesn't exist
- **500 Server Error**: Something went wrong on our end

### Response Format
All responses follow this structure:
```json
{
  "status": "success" or "error",
  "message": "Human-readable description",
  "data": "The actual information you requested",
  "errors": "Details about what went wrong (only for errors)"
}
```

---

## 6. Common Error Examples

### Missing API Key
```json
{
  "status": "error",
  "message": "API key is required",
  "errors": {
    "authorization": "Please include your API key in the Authorization header"
  }
}
```

### User Not Found
```json
{
  "status": "error", 
  "message": "User not found",
  "errors": {
    "user_id": "No user exists with ID 999"
  }
}
```

### Invalid Email Format
```json
{
  "status": "error",
  "message": "Validation failed",
  "errors": {
    "email": "Please provide a valid email address"
  }
}
```

---

## 7. Rate Limits (How many requests you can make)

To keep our service running smoothly for everyone:
- **Free accounts**: 100 requests per hour
- **Paid accounts**: 1,000 requests per hour

When you hit the limit, you'll get:
```json
{
  "status": "error",
  "message": "Rate limit exceeded",
  "errors": {
    "rate_limit": "You've made too many requests. Try again in 1 hour."
  }
}
```

---

## 8. Testing Your API (Beginner-Friendly Tools)

### Option 1: Using Postman (Visual Tool)
1. Download Postman (free)
2. Create a new request
3. Set method to GET
4. Enter URL: `https://api.yourservice.com/v1/users`
5. Add header: `Authorization: Bearer YOUR_API_KEY`
6. Click Send

### Option 2: Using curl (Command Line)
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://api.yourservice.com/v1/users
```

### Option 3: Using JavaScript (in a webpage)
```javascript
fetch('https://api.yourservice.com/v1/users', {
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

---

## 9. Best Practices for Beginners

### Do's:
✅ Always include your API key
✅ Check the response status before using data
✅ Handle errors gracefully in your code
✅ Read the documentation carefully
✅ Test with small requests first

### Don'ts:
❌ Share your API key publicly
❌ Make too many requests too quickly
❌ Assume requests will always succeed
❌ Ignore error messages
❌ Hardcode API keys in public code

---

## 10. Troubleshooting Guide

### "Unauthorized" Error
- Check if your API key is correct
- Make sure you're including it in the Authorization header
- Verify your account is active

### "Bad Request" Error
- Check your JSON format (use a JSON validator)
- Ensure required fields are included
- Verify data types (numbers vs strings)

### "Not Found" Error
- Check the URL for typos
- Verify the resource ID exists
- Ensure you're using the correct endpoint

### No Response
- Check your internet connection
- Verify the base URL is correct
- Try a simple GET request first

---

## 11. Example Use Cases

### Building a Contact List App
1. **GET /users** - Show all contacts
2. **POST /users** - Add new contact
3. **PUT /users/{id}** - Edit contact details
4. **DELETE /users/{id}** - Remove contact

### Creating a User Dashboard
1. **GET /users/{id}** - Show user profile
2. **PUT /users/{id}** - Update profile
3. **GET /users** - List all users (admin only)

---

## 12. Next Steps

Once you're comfortable with this API:
1. Explore advanced authentication (OAuth)
2. Learn about webhooks (getting notified of changes)
3. Study pagination (handling large datasets)
4. Practice with different HTTP methods
5. Build a small project using this API

---

## Support & Resources

- **Documentation**: [Link to your docs]
- **Support Email**: support@yourservice.com
- **Status Page**: [Link to status page]
- **Postman Collection**: [Download link]
- **Code Examples**: [GitHub repository]

Remember: APIs might seem complicated at first, but they're just a way for computers to talk to each other. Start small, practice with simple requests, and gradually work your way up to more complex operations!

