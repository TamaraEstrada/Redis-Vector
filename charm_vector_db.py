# pip install redis numpy
import redis
import numpy as np

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=False)

# Function to calculate cosine similarity
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Clear previous data
r.flushall()

# Charm data
# Vector dimensions: [power, range, complexity, duration]
charms = {
    "Charm1": np.array([0.3, 0.2, 0.1, 0.8], dtype=np.float32),
    "Charm2": np.array([0.6, 0.5, 0.6, 0.3], dtype=np.float32),
    "Charm3": np.array([0.9, 0.8, 0.7, 0.5], dtype=np.float32)
}

# Add charms
for charm_name, vector in charms.items():
    r.set(f"charm:{charm_name}", vector.tobytes())
    print(f"Added charm: {charm_name} with vector: {vector}")

# Query vector
query_vector = np.array([0.4, 0.3, 0.2, 0.7], dtype=np.float32)
print(f"\nQuery Vector: {query_vector}")

# Manual similarity search
results = []
for charm_name, vector in charms.items():
    similarity = cosine_similarity(query_vector, vector)
    results.append((charm_name, similarity))

# Sort and display results
results.sort(key=lambda x: x[1], reverse=True)
print("\nSimilarity Search Results:")
for charm_name, similarity in results:
    print(f"Charm: {charm_name}, Similarity: {similarity:.4f}")