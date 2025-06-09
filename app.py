from flask import Flask, render_template, request
from search_engine.indexing import DocumentIndexer
from search_engine.retrieval import SearchEngine

app = Flask(__name__)

# Initialize the indexer
indexer = DocumentIndexer('documents')
indexer.load_documents()
indexer.compute_tfidf()

# Initialize the search engine
search_engine = SearchEngine(indexer)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = []
    query = ''
    if request.method == 'POST':
        query = request.form['query']
        results = search_engine.search(query)

    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
