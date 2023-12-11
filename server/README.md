# Credit Risk API Service

This service acts as an API gateway forwarding requests to three different endpoints: Exchange Rates Service, User Identity Service, and Financial Service. It runs on http://localhost:5000.

# Makefile

This Makefile provides a set of commands to help with building, running, and managing the Credit Risk API Service.

## Prerequisites

Before using this Makefile, make sure you have the following dependencies installed:

- Docker

## Usage

Set Environment Variables

Before running the service, ensure that the necessary environment variables are set. These can be configured in the Makefile or directly in your shell.

```
export FLASK_APP=src/app/app.py
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_PORT=5000
export PYTHONPATH=$(shell pwd)
```

## Available Commands

- make start: Run the Flask application in development mode.

- make clean: Clean up any cached files (e.g., pycache).

- make build: Build the Docker image for the service.

- make run: Run the Docker container using the built image.

- make stop: Stop and remove the running Docker container.

- make create_network: Create the Docker Network "my_network"
