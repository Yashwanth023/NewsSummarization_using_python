import streamlit as st
import requests

st.title("News Summarization & Sentiment Analysis")

company = st.text_input("Enter Company Name:")
if st.button("Analyze"):
    response = requests.get(f"http://127.0.0.1:5000/fetch-news?company={company}")
    data = response.json()

    for article in data["news"]:
        st.subheader(article["title"])
        st.write(article["summary"])
        st.write(f"Sentiment: {article['sentiment']}")

    st.subheader("Overall Sentiment Analysis")
    st.json(data["sentiment"])

    if st.button("Generate Hindi Audio"):
        summary_text = " ".join([art["summary"] for art in data["news"]])
        response = requests.post("http://127.0.0.1:5000/generate-audio", json={"text": summary_text})
        audio_file = response.json()["audio_file"]
        st.audio(audio_file, format="audio/mp3")
