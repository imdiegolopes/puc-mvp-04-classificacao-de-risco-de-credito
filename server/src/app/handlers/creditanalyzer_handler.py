from flask import (
    jsonify,
    request
)
import pandas as pd
import joblib
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

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

    def handle(cls):
        try:
            input_data = request.get_json()

            # Validate input_data
            if not input_data:
                return jsonify({'error': 'Missing Params'}), 400

            categorical_cols = [f'Attribute{i}' for i in range(1, 62)]

            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
                ],
                remainder='passthrough'
            )

            input_df = pd.DataFrame({col: [input_data.get(col, 'default_value')] for col in categorical_cols})

            categorical_transformers = [('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)]
            preprocessor.transformers = categorical_transformers

            input_preprocessed = preprocessor.fit_transform(input_df)

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

