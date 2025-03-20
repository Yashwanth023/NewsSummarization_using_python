import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
import spacy

# Load spaCy model for topic extraction
nlp = spacy.load("en_core_web_sm")

def fetch_news(company_name):
    """Fetches the latest news articles related to a company."""
    API_KEY = "905f944a5c4446a1a777a2352aeefd9e"  # Replace with your NewsAPI key
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={API_KEY}"
    
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}
    
    articles = response.json().get("articles", [])[:10]  # Get top 10 articles
    news_data = []
    
    for article in articles:
        title = article["title"]
        summary = article["description"] if article["description"] else "No Summary"
        topics = extract_topics(summary)
        sentiment = analyze_sentiment(summary)
        news_data.append({"title": title, "summary": summary, "topics": topics, "sentiment": sentiment})
    
    return news_data

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text using VADER."""
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)['compound']
    return "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"

def comparative_analysis(news_data):
    """Conducts a comparative analysis of sentiment across multiple articles."""
    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in news_data:
        sentiment_count[article["sentiment"]] += 1
    
    return sentiment_count

def extract_topics(text):
    """Extracts key topics from a given text using Named Entity Recognition (NER)."""
    doc = nlp(text)
    topics = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "GPE", "PRODUCT"]]
    return list(set(topics))

def text_to_speech(text, filename="output.mp3"):
    """Converts given text to Hindi speech and saves it as an audio file."""
    tts = gTTS(text, lang="hi")
    tts.save(filename)
    return filename

