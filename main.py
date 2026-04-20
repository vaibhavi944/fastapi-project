# main.py

from fastapi import FastAPI
# import FastAPI class from the library

# create the app
# this is like opening your restaurant
app = FastAPI()
# everything revolves around this "app" object


# ─────────────────────────────────────────────────
# ENDPOINT 1: GET /
# the simplest possible endpoint
# ─────────────────────────────────────────────────

@app.get("/")
# ↑ this is a DECORATOR
# it tells FastAPI:
# "when someone sends a GET request to /"
# "run the function below"

def home():
    return {"message": "Hello World!"}
    # return a dictionary → FastAPI auto converts to JSON
    # response will be: {"message": "Hello World!"}


# ─────────────────────────────────────────────────
# ENDPOINT 2: GET /about
# ─────────────────────────────────────────────────

@app.get("/about")
def about():
    return {
        "app": "FastAPI Learning",
        "version": "1.0",
        "language": "Python"
    }
    # you can return any dictionary!
    # FastAPI converts it to JSON automatically


# ─────────────────────────────────────────────────
# ENDPOINT 3: GET /greet with a parameter
# ─────────────────────────────────────────────────

@app.get("/greet")
def greet(name: str):
    # name: str → this is a QUERY PARAMETER
    # user passes it in the URL like this:
    # /greet?name=Vaibhavi    #         ↑
    #    query parameter

    return {"message": f"Hello {name}! Welcome to FastAPI!"}
    # if name="Vaibhav"
    # response: {"message": "Hello Vaibhavi! Welcome to FastAPI!"}


# ─────────────────────────────────────────────────
# ENDPOINT 4: GET /add with two parameters
# ─────────────────────────────────────────────────

@app.get("/add")
def add(a: int, b: int):
    # two query parameters, both integers
    # URL: /add?a=5&b=3
    #           ↑   ↑
    #     use & to separate multiple params

    result = a + b
    return {
        "a": a,
        "b": b,
        "result": result
    }
    # response: {"a": 5, "b": 3, "result": 8}


# ─────────────────────────────────────────────────
# ENDPOINT 5: POST /greet
# user sends data in the BODY not the URL
# ─────────────────────────────────────────────────

from pydantic import BaseModel
# pydantic helps us define what the
# request body should look like

class GreetRequest(BaseModel):
    # this is a "schema" — defines expected input
    name: str
    age: int
    # FastAPI uses this to:
    # 1. validate incoming data
    # 2. show docs automatically
    # 3. give you proper error if data is wrong


@app.post("/greet")
def greet_post(data: GreetRequest):
    # data: GreetRequest → FastAPI reads the request body
    # and fills in the GreetRequest object for you!

    return {
        "message": f"Hello {data.name}!",
        "your_age": data.age,
        "next_year": data.age + 1
    }
    # if body was {"name": "Vaibhavi", "age": 22}
    # response: {
    #   "message": "Hello Vaibhavi!",
    #   "your_age": 22,
    #   "next_year": 23
    # }