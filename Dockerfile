# Use the official Python base image
FROM python:3.9.13

# Set the working directory inside the container
WORKDIR /app


# Copy the requirements file 
COPY requirements.txt .

# Install virtualenv
RUN pip install virtualenv

# Create a virtual environment and activate it
RUN virtualenv venv
RUN /bin/bash -c "source venv/bin/activate"

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the API script and model into the container
COPY api.py .
COPY Model/model.h5 ./Model/model.h5

# Expose the port that FastAPI will run on
EXPOSE 8000

# Define the command to run your FastAPI application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]