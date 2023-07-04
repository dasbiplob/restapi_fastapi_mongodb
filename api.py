from venv import logger
from fastapi import FastAPI
from pymongo import MongoClient

# MongoDB connection information
mongodb_host = '127.0.0.1'
mongodb_port = 27017
mongodb_database = 'mqttpy'
mongodb_collection = 'mqttpy'

# Create a FastAPI instance
app = FastAPI()

try:
    # MongoDB connection client
    client = MongoClient(mongodb_host, mongodb_port)
    db = client[mongodb_database]
    collection = db[mongodb_collection]
except Exception as e:
    logger.error(f"Error connecting to MongoDB: {str(e)}")
    # Handle the error appropriately (e.g., log, raise, or return an error response)

# Endpoint to get all messages
@app.get("/messages")
def get_all_messages():
    try:
        messages = list(collection.find())
        # Convert MongoDB ObjectId to string representation
        for message in messages:
            message["_id"] = str(message["_id"])
        return {"messages": messages}
    except Exception as e:
        logger.error(f"Error retrieving messages: {str(e)}")
        # Handle the error appropriately (e.g., log, raise, or return an error response)
