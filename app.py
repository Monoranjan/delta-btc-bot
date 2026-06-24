from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Delta BTC Bot Running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    print("Received:", data)

    action = data.get("action")

    if action == "buy":
        print("BUY SIGNAL RECEIVED")

    elif action == "sell":
        print("SELL SIGNAL RECEIVED")

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
