from flask import (
    jsonify,
    request
)
import pandas as pd
import joblib
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Importando bibliotecas necessárias
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from ucimlrepo import fetch_ucirepo

# Mapeamento dos atributos para seus respectivos nomes
attribute_mapping = {
    'Attribute1': 'Status da conta corrente existente',
    'Attribute2': 'Duração em meses',
    'Attribute3': 'Histórico de crédito',
    'Attribute4': 'Propósito',
    'Attribute5': 'Quantidade de crédito',
    'Attribute6': 'Poupança/obrigações de títulos',
    'Attribute7': 'Emprego atual desde',
    'Attribute8': 'Taxa de parcelamento em porcentagem da renda disponível',
    'Attribute9': 'Estado civil e sexo',
    'Attribute10': 'Outros devedores/fiadores',
    'Attribute11': 'Residência atual desde',
    'Attribute12': 'Tipo de propriedade',
    'Attribute13': 'Idade',
    'Attribute14': 'Outros planos de parcelamento',
    'Attribute15': 'Tipo de moradia',
    'Attribute16': 'Número de créditos existentes neste banco',
    'Attribute17': 'Profissão',
    'Attribute18': 'Número de pessoas obrigadas a fornecer sustento',
    'Attribute19': 'Telefone',
    'Attribute20': 'Trabalhador estrangeiro'
}

# Carrega o modelo de ML
best_model_path = os.path.join(os.path.dirname(__file__), '../../data/best_credit_risk_classifier_trained_model.pkl')
best_model = joblib.load(best_model_path)

class CreditAnalyzerHandler:
    def __init__(self):
        pass

    @staticmethod
    def handle():
        try:
            default_value = {
                "Attribute1": "A11",
                "Attribute2": 12,
                "Attribute3": "A30",
                "Attribute4": "A40",
                "Attribute5": 0,
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

            request_data = request.get_json()

            input_data = {**default_value, **request_data}
            # Validate input_data
            if not input_data:
                return jsonify({'error': 'Missing Params'}), 400

            
            # fetch dataset
            statlog_german_credit_data = fetch_ucirepo(id=144)

            # Supondo que 'class' seja a coluna-alvo
            X = statlog_german_credit_data.data.features
            y = statlog_german_credit_data.data.targets['class']

            # Identificando colunas categóricas
            categorical_cols = [col for col in X.columns if X[col].dtype == 'object']

            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
                ],
                remainder='passthrough'
            )

            # Dividindo os dados em conjuntos de treino e teste
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Pré-processando os dados
            X_train_preprocessed = preprocessor.fit_transform(X_train)
            X_test_preprocessed = preprocessor.transform(X_test)

            sample_input_df = pd.DataFrame([input_data])

            # Pré-processando os dados usando o mesmo transformer usado no treinamento
            input_preprocessed = preprocessor.transform(sample_input_df)            
            prediction = best_model.predict(input_preprocessed)

            mapped_response = {attribute_mapping[key]: input_data[key] for key in input_data}

            result = {
                'prediction': int(prediction[0]),
                'class': 'Bad' if prediction[0] == 2 else 'Good',
                'mapped_response': mapped_response
            }

            return jsonify(result)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

