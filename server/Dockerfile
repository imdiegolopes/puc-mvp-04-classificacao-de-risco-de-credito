# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install make (or any other necessary dependencies)
RUN apt-get update && \
    apt-get install -y make && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port available to the world outside this container
EXPOSE 5000

CMD ["make", "start"]
