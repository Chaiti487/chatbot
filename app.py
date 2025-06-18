from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Invalid or missing JSON"}), 400
        print(data)
        return jsonify({"message": "Hello", "received_data": data}), 200
    else:
        return jsonify({"message": "Send a POST request with JSON"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
