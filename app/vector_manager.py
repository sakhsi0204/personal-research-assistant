import faiss
import numpy as np


class VectorManager:

    def __init__(self):
        self.index = None
        self.text_chunks = []

    def create_embeddings(self, chunks):

        self.text_chunks = chunks

        embeddings = []

        for chunk in chunks:

            vector = np.zeros(128)

            words = chunk.split()

            for i, word in enumerate(words[:128]):
                vector[i] = len(word)

            embeddings.append(vector)

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(
            embeddings
        )

        return len(chunks)

    def search(self, query, top_k=3):

        query_vector = np.zeros(
            (1, 128),
            dtype=np.float32
        )

        words = query.split()

        for i, word in enumerate(words[:128]):
            query_vector[0][i] = len(word)

        distances, indices = self.index.search(
            query_vector,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx < len(self.text_chunks):
                results.append(
                    self.text_chunks[idx]
                )

        return results