from handlers.healthcheck_handler import HealthcheckHandler
from handlers.creditanalyzer_handler import CreditAnalyzerHandler
from flask import (
    Flask
)
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule('/', 'index', HealthcheckHandler.handle, methods=['GET'])
app.add_url_rule('/v1/credit-analyzer', 'credit_analyzer',
                 CreditAnalyzerHandler.handle, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8081, host="0.0.0.0")
