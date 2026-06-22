from vector_manager import VectorManager

chunks = [
    "Artificial Intelligence is transforming healthcare.",
    "Machine Learning is a subset of AI.",
    "Deep Learning uses neural networks.",
    "Python is widely used for AI development.",
    "FAISS helps perform similarity search."
]

vm = VectorManager()

print("Creating embeddings...")
vm.create_embeddings(chunks)

print("Embeddings created successfully!")

query = "What is machine learning?"

results = vm.search(query)

print("\nSearch Results:\n")

for i, result in enumerate(results, start=1):
    print(f"Result {i}:")
    print(result)
    print()