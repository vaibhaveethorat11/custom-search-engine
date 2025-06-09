import re
from sklearn.metrics.pairwise import cosine_similarity

class SearchEngine:
    def __init__(self, indexer):
        self.indexer = indexer

    def highlight_snippet(self, text, query):
        query_words = query.lower().split()
        snippet = ''
        for sentence in text.split('.'):
            if any(q in sentence.lower() for q in query_words):
                snippet = sentence.strip()
                break
        if not snippet:
            snippet = text[:200]

        for q in query_words:
            snippet = re.sub(f'(?i)({q})', r'<mark>\1</mark>', snippet)
        return snippet

    def search(self, query, top_k=5):
        query_vec = self.indexer.vectorizer.transform([query])
        similarity = cosine_similarity(query_vec, self.indexer.doc_vectors).flatten()
        ranked_indices = similarity.argsort()[::-1][:top_k]

        results = []
        for idx in ranked_indices:
            snippet = self.highlight_snippet(self.indexer.docs[idx], query)
            results.append({
                'doc_name': self.indexer.doc_names[idx],
                'score': round(similarity[idx], 3),
                'snippet': snippet
            })
        return results
