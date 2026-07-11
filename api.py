"""Simple FastAPI example with two GET endpoints.

* ``GET /welcome`` – returns a static greeting.
* ``GET /user`` – accepts optional query parameters and returns them as a
  JSON dictionary.  This demonstrates how to pass simple values without any
  Pydantic models.

Run the server with ``uvicorn api:app --reload`` from the ``c:\dev\api``
directory.
"""

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/welcome")
def welcome() -> dict:
  """Return a friendly welcome message."""
  return {"message": "Welcome to the FastAPI demo!"}


@app.get("/user")
def get_userprofile():
  return {

    "name":"Nandha",
    "Emailid":"nandhagopalac@gmail.com",
    "linkedin":"www.linkedin.com/in/nandhagopalac"

  }