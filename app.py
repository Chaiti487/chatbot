from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    print(data)
    return jsonify({"message": "Hello"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)