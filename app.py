from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

def chat_with_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    response = chat_with_ollama(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
