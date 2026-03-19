from flask import Flask, request, jsonify

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I didn't understand that."

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()