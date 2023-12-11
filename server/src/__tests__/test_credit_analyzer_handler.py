from flask import Flask
import pytest
import json

from src.app.handlers.creditanalyzer_handler import CreditAnalyzerHandler

@pytest.fixture
def app():
    return Flask(__name__)

def test_credit_analyzer_handler_returns_valid_response(app):
    handler = CreditAnalyzerHandler()

    input_data = {
            "Attribute1": "A12",
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
            "Attribute20": "A202"
        }
    with app.test_request_context(
        method='POST',
        json=input_data,
        content_type='application/json',
        path='/v1/analyze_credit'
    ):
        response = handler.handle()

    # Verifique se a resposta contém as informações esperadas
    assert 'prediction' in response.json
    assert 'class' in response.json
    assert 'mapped_response' in response.json
    assert response.status_code == 200  # Verifique se o código de status é 200 para uma resposta bem-sucedida

def test_credit_analyzer_handler_returns_valid_response_good_class(app):
    handler = CreditAnalyzerHandler()

    input_data = {
        "Attribute1": "A13",
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
        "Attribute20": "A202"
    }

    with app.test_request_context(
        method='POST',
        json=input_data,
        content_type='application/json',
        path='/v1/analyze_credit'
    ):
        response = handler.handle()

    assert response.status_code == 200
    assert response.json['class'] == 'Good'
    assert response.json['prediction'] == 1

def test_credit_analyzer_handler_returns_valid_response_bad_class(app):
    handler = CreditAnalyzerHandler()

    input_data = {
        "Attribute1": "A11",
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
        "Attribute20": "A202"
    }

    input_data['Attribute5'] = 1000000

    with app.test_request_context(
        method='POST',
        json=input_data,
        content_type='application/json',
        path='/v1/analyze_credit'
    ):
        response = handler.handle()

    assert response.status_code == 200
    assert response.json['class'] == 'Bad'
    assert response.json['prediction'] == 2

