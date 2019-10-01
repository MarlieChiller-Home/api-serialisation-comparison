from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def tester():
    payload = request.get_json()
    print(type(payload))
    return jsonify({"status_code": 200})
