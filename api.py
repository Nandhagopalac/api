"""Simple FastAPI example with two GET endpoints.

* ``GET /welcome`` – returns a static greeting.
* ``GET /user`` – accepts optional query parameters and returns them as a
  JSON dictionary.  This demonstrates how to pass simple values without any
  Pydantic models.

Run the server with ``uvicorn api:app --reload`` from the ``c:\dev\api``
directory.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


API_KEY = "123ABCDFG234"
@app.middleware("http")
async def check_api_key(request,call_next):
  key = request.headers.get("X-API-KEY")
  if key != API_KEY:
    return JSONResponse(status_code=401,content={"error":"Unauthorised"})
  return await call_next(request)


# Root Endpoint
@app.get("/welcome")
def welcome() -> dict:
  """Return a friendly welcome message."""
  return {"message": "Welcome to the FastAPI demo!"}

# Get api with parameter
@app.get("/user")
def get_userprofile():
  return {

    "name":"Nandha",
    "Emailid":"nandhagopalac@gmail.com",
    "linkedin":"www.linkedin.com/in/nandhagopalac"

  }
@app.get("/user/{user_id}")
def user_profile(user_id:int):
  if (user_id==1):
    return {
          "name":"Nandha",
    "Emailid":"nandhagopalac@gmail.com",
    "linkedin":"www.linkedin.com/in/nandhagopalac"
    }
  else:
    return{
            "name":"Agalya"+str(user_id),
    "Emailid":"nandhagopalac@gmail.com",
    "linkedin":"www.linkedin.com/in/nandhagopalac"
    }
  
{
  "name":"gopal",
  "age":23,
  "email":"nandhagopalac@gmail.com"
}

class User(BaseModel):
    name:str
    age:int
    email:str

# Create new entry
users = []
@app.post("/users")
def create_user(user:User):
  users.append(user.dict())
  return {"message":"User added successfully","total_users":len(users)}