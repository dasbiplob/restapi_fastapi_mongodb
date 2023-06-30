from fastapi import FastAPI
from pymongo import MongoClient

# MongoDB connection information
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'mqttpy'
mongodb_collection = 'mqttpy'

# Create a FastAPI instance
app = FastAPI()

# MongoDB connection client
client = MongoClient(mongodb_host, mongodb_port)
db = client[mongodb_database]
collection = db[mongodb_collection]

# Endpoint to get all messages
@app.get("/messages")
def get_all_messages():
    messages = list(collection.find())
    # Convert MongoDB ObjectId to string representation
    for message in messages:
        message["_id"] = str(message["_id"])
    return {"messages": messages}
