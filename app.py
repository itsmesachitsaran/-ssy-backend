from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route("/predict/<stock>")
def predict(stock):
    data = yf.download(stock + ".NS", period="6mo")

    if data.empty:
        return jsonify({"error": "Wrong stock name"})

    close = data["Close"].iloc[-1]
    ma20 = data["Close"].rolling(20).mean().iloc[-1]

    if close > ma20:
        trend = "Bullish"
        confidence = "65%"
    else:
        trend = "Bearish"
        confidence = "60%"

    return jsonify({
        "stock": stock.upper(),
        "trend": trend,
        "confidence": confidence
    })

app.run(host="0.0.0.0", port=10000)
