from flask import (
    jsonify,
    request
)
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

attribute_mapping = {
    'Attribute1': 'Status of existing checking account',
    'Attribute2': 'Duration in months',
    'Attribute3': 'Credit history',
    'Attribute4': 'Purpose',
    'Attribute5': 'Credit amount',
    'Attribute6': 'Savings account/bonds',
    'Attribute7': 'Present employment since',
    'Attribute8': 'Installment rate in percentage of disposable income',
    'Attribute9': 'Personal status and sex',
    'Attribute10': 'Other debtors / guarantors',
    'Attribute11': 'Present residence since',
    'Attribute12': 'Property',
    'Attribute13': 'Age',
    'Attribute14': 'Other installment plans',
    'Attribute15': 'Housing',
    'Attribute16': 'Number of existing credits at this bank',
    'Attribute17': 'Job',
    'Attribute18': 'Number of people being liable to provide maintenance for',
    'Attribute19': 'Telephone',
    'Attribute20': 'Foreign worker'
}

class CreditAnalyzerHandler:
    def __init__(self):
        pass

    def handle():
        try:

            input_data = request.get_json()
            categorical_cols = [f'Attribute{i}' for i in range(1, 62)]

            # Recreate the preprocessor in the deployment environment
            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
                ],
                remainder='passthrough'
            )

            # Load the best model
            best_model_path = os.path.join(os.path.dirname(__file__), '../../data/best_credit_risk_classifier_trained_model.pkl')
            best_model = joblib.load(best_model_path)
            # Get JSON input from the request

            # Create DataFrame with default values for all categorical columns
            input_df = pd.DataFrame({col: [input_data.get(col, 'default_value')] for col in categorical_cols})

            categorical_transformers = [('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)]
            preprocessor.transformers = categorical_transformers

            # Preprocess the input data using the recreated preprocessor
            input_preprocessed = preprocessor.fit_transform(input_df)

            # Make predictions using the best model
            prediction = best_model.predict(input_preprocessed)

            # Map attribute names for response
            mapped_response = {attribute_mapping[key]: input_data[key] for key in input_data}
            
            # Return the result as JSON
            result = {
                'prediction': int(prediction[0]),
                'class': 'Bad' if prediction[0] == 2 else 'Good',
                'mapped_response': mapped_response
            }

            return jsonify(result)

        except Exception as e:
            return jsonify({'error': str(e)}), 500

