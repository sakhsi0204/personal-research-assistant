from vector_manager import VectorManager

chunks = [
    "Transformers are deep learning models used in NLP.",
    "Attention mechanism helps models focus on important words.",
    "BERT is a transformer-based language model.",
    "GPT generates human-like text.",
    "Deep learning uses neural networks."
]

vector_db = VectorManager()

vector_db.create_embeddings(chunks)

results = vector_db.search(
    "What are transformers?"
)

print("\nSEARCH RESULTS:\n")

for r in results:
    print(r)