# Use the official Python base image
FROM python:3.11.4

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files to the working directory
COPY . .

# Expose the port that your application will listen on
EXPOSE 8000

# Start the FastAPI server when the container starts
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
