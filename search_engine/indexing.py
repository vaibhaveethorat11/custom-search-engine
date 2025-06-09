import os
from sklearn.feature_extraction.text import TfidfVectorizer

class DocumentIndexer:
    def __init__(self, folder_path='documents'):
        self.folder_path = folder_path
        self.docs = []
        self.doc_names = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.doc_vectors = None

    def load_documents(self):
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.txt'):
                with open(os.path.join(self.folder_path, filename), 'r', encoding='utf-8') as f:
                    self.docs.append(f.read())
                    self.doc_names.append(filename)
        return self.docs

    def compute_tfidf(self):
        self.doc_vectors = self.vectorizer.fit_transform(self.docs)
        return self.doc_vectors
