# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files to the working directory
COPY api.py .
COPY mqtt_mongodb.py .  

# Expose the port that your application will listen on
EXPOSE 8080

# Start the FastAPI server when the container starts
CMD ["uvicorn","api:app", "--host", "0.0.0.0", "--port", "8080"]
