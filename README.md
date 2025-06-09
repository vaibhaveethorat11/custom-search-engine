# 🧠 Custom Search Engine

A lightweight Google-style search engine built using Python, Flask, and scikit-learn. This engine indexes `.txt` documents, vectorizes them with TF-IDF, and ranks them using cosine similarity — complete with a modern Bootstrap UI, light/dark mode toggle, query highlighting, and fuzzy matching for misspelled words.

---

## 🚀 Features

- 🔍 **TF-IDF based document ranking**
- 🔦 **Snippet extraction with highlighted search terms**
- 🌓 **Light/Dark Mode toggle**
- 🧠 **Fuzzy matching** for approximate search queries
- 💻 **Bootstrap-based clean UI**

---

## 📂 Folder Structure

```plaintext
custom-search-engine/
├── app.py
├── documents/               # .txt files for search corpus
├── templates/
│   └── index.html           # HTML frontend
├── search_engine/
│   ├── indexing.py          # TF-IDF logic
│   └── retrieval.py         # Search, scoring, fuzzy logic
├── requirements.txt
└── README.md

````
---
## 🛠️ Setup Instructions

**1. Clone the repository:**
git clone https://github.com/YOUR_USERNAME/custom-search-engine.git
cd custom-search-engine

**2. Create and activate virtual environment:**
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate (Windows)

**3. Install dependencies:**
pip install -r requirements.txt

**4. Add your documents:**
Place .txt files inside the documents/ folder. These will be indexed and searched.

**5. Run the app:**
python app.py
Visit: http://localhost:5000

---

## 🧠 **Example Queries**

Try:

machine learning

artificial intelegnce (with typo — fuzzy match handles it)
