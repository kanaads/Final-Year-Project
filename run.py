from flask import Flask, render_template, request
import requests
import math
import text_filter as filter
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

def ngrams(input_text, n):
    input_text = input_text.lower().replace(" ", "")
    return [input_text[i:i+n] for i in range(len(input_text)-n+1)]

def ngram_containment(ngram_query, ngram_doc):
    ngram_query = set(ngram_query)
    ngram_doc = set(ngram_doc)
    return len(ngram_query.intersection(ngram_doc)) / float(len(ngram_query)) if ngram_query else 0.0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    input_text = request.form['input_text']
    clean_query = filter.removeStopWord(input_text)
    print("🔍 Cleaned Query:", clean_query)

    params = {
        "engine": "google",
        "q": clean_query,
        "num": 4,
        "api_key": os.getenv("SERPAPI_KEY")
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        print("🧾 Raw SerpAPI results:", results)
        links = [res['link'] for res in results.get("organic_results", [])]
        print("🔗 Extracted links:", links)
    except Exception as e:
        print(f"❌ SerpAPI error: {e}")
        links = []

    similarity_results = []
    ngram_query = set(ngrams(input_text, 4))

    for link in links:
        try:
            response = requests.get(link, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.get_text()
            containment = ngram_containment(ngram_query, set(ngrams(content, 4)))
            similarity_results.append({'url': link, 'containment': containment})
        except Exception as e:
            print(f"❌ Error processing {link}: {e}")

    print("✅ Final similarity results:", similarity_results)
    return render_template('results.html', similarity_results=similarity_results)

if __name__ == '__main__':
    app.run(debug=True)
