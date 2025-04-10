from flask import Flask, request, jsonify, send_file
from chatbot import simple_chatbot  # Import your chatbot function

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing "message" in request'}), 400

    user_message = data['message']
    response = simple_chatbot(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Try port 5001