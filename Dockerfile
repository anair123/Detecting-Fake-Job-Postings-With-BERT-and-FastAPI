# Use the official Python base image
FROM python:3.9.13-slim

# Set the working directory inside the container
WORKDIR /app


# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
