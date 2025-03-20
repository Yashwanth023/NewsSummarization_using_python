# News Summarization & Sentiment Analysis

## 🚀 Project Overview
This project is a **web-based application** that extracts news articles about a company, performs **sentiment analysis**, generates a comparative sentiment report, and converts the summary into **Hindi audio** using Text-to-Speech (TTS).

---

## 📌 Features
- ✅ **News Extraction**: Fetches the latest news articles about a company.
- ✅ **Sentiment Analysis**: Determines whether the news is **Positive, Negative, or Neutral**.
- ✅ **Comparative Analysis**: Compares sentiment across multiple articles.
- ✅ **Hindi Text-to-Speech**: Converts the sentiment summary into **Hindi audio**.
- ✅ **Interactive UI**: Built with **Streamlit**.

---

## 🛠️ Tech Stack
- **Backend:** Flask, BeautifulSoup, TextBlob, VaderSentiment, gTTS
- **Frontend:** Streamlit
- **Database:** N/A (Fetching live news dynamically)

---

## 📂 Project Structure
```
NewsSummarization/
│── api.py          # Flask API for news extraction, sentiment analysis & TTS
│── app.py          # Streamlit frontend
│── utils.py        # Helper functions for processing
│── requirements.txt # Dependencies
│── README.md       # Documentation
```

---

## 🔧 Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Yashwanth023/NewsSummarization_using_python.git
cd news-summarization
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate (Mac/Linux)
venv\Scripts\activate  # Activate (Windows)

pip install -r requirements.txt  # Install dependencies
```

### **3️⃣ Run the Flask Backend**
```bash
python api.py
```
- Check if it's running: Open **http://127.0.0.1:5000/fetch-news?company=Nike** in your browser.

### **4️⃣ Run the Streamlit Frontend**
```bash
streamlit run app.py
```
- Open the displayed URL to access the UI.

---

## 📤 API Endpoints
### **1️⃣ Fetch News & Sentiment Analysis**
```http
GET /fetch-news?company=Tesla
```
📌 **Response:**
```json
{
  "news": [
    {
      "title": "Tesla's stock surges",
      "summary": "Tesla sees record sales...",
      "sentiment": "Positive",
      "topics": ["Stock Market", "EV"]
    }
  ],
  "sentiment": {"Positive": 5, "Negative": 3, "Neutral": 2}
}
```

### **2️⃣ Generate Hindi Audio**
```http
POST /generate-audio
```
📌 **Request Body:**
```json
{
  "text": "Tesla's latest news is mostly positive."
}
```
📌 **Response:**
```json
{
  "audio_file": "output.mp3"
}
```

---

## 🚀 Deployment on Hugging Face Spaces
1. **Push Code to GitHub**
```bash
git add .
git commit -m "Initial Commit"
git push origin main
```
2. **Create a New Hugging Face Space** (one for **backend** & one for **frontend**).
3. **For Backend:** Select **Docker** and link to GitHub.
4. **For Frontend:** Select **Streamlit** and link to GitHub.
5. **Deploy & Test!** 🎉

---

## ⚠️ Troubleshooting
### **1️⃣ API Not Connecting to Streamlit?**
- Ensure **Flask API (`api.py`) is running** before starting Streamlit.
- Check the **API URL** in `app.py`. If deployed, use **Hugging Face API URL**.

### **2️⃣ `gTTS` Not Generating Audio?**
- Ensure `gTTS` is installed: `pip install gtts`.
- Try running:
  ```python
  from gtts import gTTS
  tts = gTTS("Hello", lang="hi")
  tts.save("test.mp3")
  ```

---

## ✨ Future Improvements
- **Improve Sentiment Analysis** using a deep-learning model (e.g., `transformers`).
- **Add More Language Support** for TTS.
- **Enhance UI** with more interactive elements.

---



