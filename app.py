from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route("/")
def home():
    return "SSY backend running"

@app.route("/predict/<stock>")
def predict(stock):
    try:
        data = yf.download(
            stock + ".NS",
            period="6mo",
            progress=False
        )

        if data.empty:
            return jsonify({"error": "Invalid NSE stock"})

        close = float(data["Close"].iloc[-1])
        ma20 = float(data["Close"].rolling(20).mean().iloc[-1])

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

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
