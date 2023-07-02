# restapi_fastapi_mongodb
QTT to MongoDB Integration
# Prerequisites
Before running the application, make sure you have the following prerequisites installed:

- Python 3
- Paho MQTT library (`paho-mqtt`)
- FastAPI (`fastapi`)
- PyMongo library (`pymongo`)
You can install the required Python libraries using pip3:

pip3 install paho-mqtt fastapi pymongo

## Running the Application

To run the application, follow these steps:

1. Start the MQTT to MongoDB integration script by running `mqtt_mongodb.py`:
    python mqtt_mongodb.py

This script establishes a connection to the MQTT broker, subscribes to the specified topic, and saves received MQTT messages to the MongoDB collection.

2. In a separate terminal, start the FastAPI server by running `api.py`:
    uvicorn index:app --reload

The FastAPI server exposes an endpoint to retrieve all the messages stored in the MongoDB collection.

3. Access the API endpoint:

Open a web browser or use a tool like cURL to access the following URL:

http://localhost:8080/docs#/default/get_all_messages_messages_get
or
http://localhost:8080/messages

