from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import fetch_news, comparative_analysis, text_to_speech

app = Flask(__name__)
CORS(app)

@app.route("/fetch-news", methods=["GET"])
def get_news():
    company = request.args.get("company")
    news_data = fetch_news(company)
    sentiment_data = comparative_analysis(news_data)
    return jsonify({"news": news_data, "sentiment": sentiment_data})

@app.route("/generate-audio", methods=["POST"])
def generate_audio():
    text = request.json.get("text")
    filename = text_to_speech(text)
    return jsonify({"audio_file": filename})

if __name__ == "__main__":
    app.run(debug=True)
