from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_topics(text):
    lines = [line.strip() for line in text.split("\n") if len(line.strip()) > 5]

    embeddings = model.encode(lines)

    unique_topics = []
    unique_embeddings = []

    for i, emb in enumerate(embeddings):
        if not unique_embeddings:
            unique_topics.append(lines[i])
            unique_embeddings.append(emb)
            continue

        sims = cosine_similarity([emb], unique_embeddings)[0]

        if max(sims) < 0.85:
            unique_topics.append(lines[i])
            unique_embeddings.append(emb)

    return unique_topics