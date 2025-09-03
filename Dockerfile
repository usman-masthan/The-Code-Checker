# Dockerfile
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application file into the container
COPY app.py .

# Define the command to run when the container starts
CMD ["python", "app.py"]