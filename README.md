# 🧠 Plagiarism Detection Tool

This is a Flask-based web application that performs **plagiarism detection using n-gram containment** and Google Search results (via SerpAPI). The tool processes input text, extracts meaningful content, and compares it against top search results for similarity scoring.

---

### 🔗 Live Demo

🌐 [Try it here](https://plagiarism-detection-tool-b882f7530dfd.herokuapp.com/)  
_(Hosted on Heroku)_

---

### 🚀 Features

- 🔍 Google Search via SerpAPI
- 🧪 N-gram containment similarity scoring
- 📊 Displays similarity % for top sources
- 🌐 Web interface with Bootstrap styling
- 🌀 Spinner loader while search is processing
- ✅ Works well on mobile and desktop

---

### 📁 Project Structure

Final-Year-Project/ ├── run.py # Main Flask application ├── text_filter.py # NLP utilities for stopword removal and POS tagging ├── requirements.txt # Python dependencies for deployment and local use ├── Procfile # Tells Heroku how to start the app ├── runtime.txt # (Optional) Specifies Python version for Heroku ├── .env # Environment variables (e.g., SerpAPI key – not committed) └── templates/ ├── index.html # Search input form with Bootstrap styling and spinner └── results.html # Displays similarity results in a styled table

---

### 🧪 How It Works

1. **User submits** a block of text through the web form.
2. The app **cleans the text** using NLTK:
   - Converts to lowercase
   - Removes stopwords
   - Keeps only relevant parts of speech (nouns, verbs, adjectives)
3. The cleaned query is sent to **SerpAPI**, which returns the top 4 Google search results.
4. Each result is fetched and parsed using **BeautifulSoup**.
5. The app computes **n-gram containment** between the input and each result.
6. A table is shown with:
   - 🔗 Source URLs (clickable)
   - 📊 Similarity percentages

