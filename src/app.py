
from flask import Flask
from compute import validate_and_calculate

app = Flask(__name__)

@app.route('/compute/<operation>', methods=['GET'])
def compute(operation):
    result, status_code = validate_and_calculate(operation)
    response = {
        "Result": result,
        "Status Code": status_code
    }
    return response, 200