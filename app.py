from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "SSY backend running"

@app.route("/predict/<stock>")
def predict(stock):
    return jsonify({
        "stock": stock.upper(),
        "trend": "Bullish",
        "confidence": "60%"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
