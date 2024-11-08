import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# MongoDB URI from the .env file
MONGO_URI = os.getenv("MONGO_URI")

# Initialize the MongoDB client
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Access the specific database
database = client["sample_mflix"]  # Replace "sample_mflix" with your database name
user_collection = database.get_collection("users")  # Replace "users" with your collection name

# Helper function to format user data
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        # Add more fields as needed
    }

# Function to retrieve all users
def retrieve_users():
    users = []
    for user in user_collection.find().limit(10):
        users.append(user_helper(user))
    return users

# Function to add a new user
def add_user(user_data: dict) -> dict:
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)
