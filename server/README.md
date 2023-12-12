# Credit Risk API Service

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

- make create_network: Create the Docker Network

- make test: Run the tests

## Run a cURL example

```
curl -X POST -H "Content-Type: application/json" -d '{
    "Attribute1": 11,
    "Attribute2": 12,
    "Attribute3": "A30",
    "Attribute4": "A40",
    "Attribute5": 5000,
    "Attribute6": "A61",
    "Attribute7": "A72",
    "Attribute8": 3,
    "Attribute9": "A92",
    "Attribute10": "A101",
    "Attribute11": 4,
    "Attribute12": "A121",
    "Attribute13": 35,
    "Attribute14": "A141",
    "Attribute15": "A151",
    "Attribute16": 12,
    "Attribute17": "A173",
    "Attribute18": 1,
    "Attribute19": "A192",
    "Attribute20": "A201"
}' http://localhost:5000/v1/analyze_credit
```

Detailed

```
curl -X POST -H "Content-Type: application/json" -d '{
    "Attribute1": 11, # Tipo da Conta
    "Attribute2": 12,     # Duração em Meses
    "Attribute3": "A30",  # Histórico de crédito (Categórico)
    "Attribute4": "A40",  # Propósito do crédito (Categórico)
    "Attribute5": 5000,   # Quantidade de crédito
    "Attribute6": "A61",  # Poupança/obrigações de títulos (Categórico)
    "Attribute7": "A72",  # Emprego atual desde (Categórico)
    "Attribute8": 3,      # Taxa de parcelamento em porcentagem da renda disponível
    "Attribute9": "A92",  # Estado civil e sexo (Categórico)
    "Attribute10": "A101",# Outros devedores/fiadores (Categórico)
    "Attribute11": 4,     # Residência atual desde
    "Attribute12": "A121",# Tipo de propriedade (Categórico)
    "Attribute13": 35,    # Idade em anos
    "Attribute14": "A141",# Outros planos de parcelamento (Categórico)
    "Attribute15": "A151",# Tipo de moradia (Categórico)
    "Attribute16": 12,     # Número de créditos existentes neste banco
    "Attribute17": "A173",# Profissão (Categórico)
    "Attribute18": 1,     # Número de pessoas obrigadas a fornecer sustento
    "Attribute19": "A192",# Telefone registrado sob o nome do cliente (Categórico)
    "Attribute20": "A201" # Trabalhador estrangeiro (Categórico)
}' http://localhost:5000/v1/analyze_credit
```
