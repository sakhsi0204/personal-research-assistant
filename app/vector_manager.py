from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class VectorManager:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.text_chunks = []
        self.vectors = None

    def create_embeddings(self, chunks):
        self.text_chunks = chunks
        self.vectors = self.vectorizer.fit_transform(chunks)

    def search(self, query, top_k=3):

        query_vector = self.vectorizer.transform([query])

        similarities = cosine_similarity(
            query_vector,
            self.vectors
        )[0]

        ranked = similarities.argsort()[::-1]

        results = []

        for idx in ranked[:top_k]:
            results.append(self.text_chunks[idx])

        return results