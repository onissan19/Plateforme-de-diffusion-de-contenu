# Use an official Python runtime as a parent image 

FROM python:3.11-slim

 

# Set the working directory 

WORKDIR /app 

 

# Copy the current directory contents into the container at /app 

COPY . /app 

 

# Install dependencies 

RUN pip install -r requirements.txt 

 

# Make port 5000 available to the world outside the container 

EXPOSE 5000 

 

# Run the application 

CMD ["python3", "app.py"] 