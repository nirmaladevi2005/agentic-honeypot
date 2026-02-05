from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def honeypot():
    return jsonify({
        "status": "Agentic Honey-Pot is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
