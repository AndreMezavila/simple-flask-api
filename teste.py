
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/data', methods=['POST'])
def get_data():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    return jsonify({'received_data': data}), 200
  