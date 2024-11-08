from fastapi import FastAPI
from database import retrieve_users, add_user

app = FastAPI()

@app.get("/users", response_description="List all users")
def get_users():
    users = retrieve_users()
    return {"users": users}

@app.post("/users", response_description="Add new user")
def create_user(user: dict):
    new_user = add_user(user)
    return {"user": new_user}
