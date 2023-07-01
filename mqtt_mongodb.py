import json
import time
import datetime
import paho.mqtt.client as mqtt
from pymongo import MongoClient

# MQTT broker information
mqtt_broker = 'localhost'
mqtt_topic = 'charger/1/connector/1/session/1'

# MongoDB connection information
mongodb_host = 'localhost'
mongodb_port = 27017
mongodb_database = 'mqttpy'
mongodb_collection = 'mqttpy'

# MQTT callback when a message is received
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
        print(f"Received MQTT message: {payload} at {datetime.datetime.now()}")

        # Save the message to the database
        save_to_database(payload)
    except Exception as e:
        print(f"An error occurred while processing the MQTT message: {e}")

# Function to save the message to MongoDB
def save_to_database(payload):
    try:
        client = MongoClient(mongodb_host, mongodb_port)
        db = client[mongodb_database]
        collection = db[mongodb_collection]
        data = json.loads(payload)
        collection.insert_one(data)
        print('Data saved to MongoDB!')
        client.close()
    except Exception as e:
        print(f"An error occurred while saving to the database: {e}")

# Create an MQTT client and connect to the broker
client = mqtt.Client()

try:
    client.connect(mqtt_broker)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# Set the callback function for MQTT messages
client.on_message = on_message

# Subscribe to the MQTT topic
try:
    client.subscribe(mqtt_topic)
except Exception as e:
    print(f"Failed to subscribe to MQTT topic: {e}")
    exit(1)

# Start the MQTT loop
try:
    client.loop_start()
except KeyboardInterrupt:
    # Gracefully handle Ctrl+C termination
    client.loop_stop()

# Publish new sessions every 1 minute
try:
    while True:
        # Create a new session payload
        session_id = 1
        energy_delivered = 30
        duration = 45
        session_cost = 70
        payload = {
            "session_id": session_id,
            "energy_delivered_in_kWh": energy_delivered,
            "duration_in_seconds": duration,
            "session_cost_in_cents": session_cost
        }

        # Publish the new session payload to the MQTT topic
        try:
            client.publish(mqtt_topic, json.dumps(payload))
        except Exception as e:
            print(f"Failed to publish MQTT message: {e}")

        # Wait for 1 minute
        time.sleep(60)
except KeyboardInterrupt:
    pass

# Disconnect from the MQTT broker
client.loop_stop()
client.disconnect()
