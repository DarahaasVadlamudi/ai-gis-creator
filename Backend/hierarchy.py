from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_hierarchy(topics):
    if len(topics) < 3:
        return {"General": {"topics": topics}}

    embeddings = model.encode(topics)

    kmeans = KMeans(n_clusters=min(3, len(topics)))
    labels = kmeans.fit_predict(embeddings)

    hierarchy = {}

    for i, label in enumerate(labels):
        gt = f"GT{label+1}"

        if gt not in hierarchy:
            hierarchy[gt] = {"topics": []}

        hierarchy[gt]["topics"].append({
            "name": topics[i],
            "subtopics": []
        })

    return {
    "GTs": [
        {
            "name": gt,
            "topics": hierarchy[gt]["topics"]
        }
        for gt in hierarchy
    ]
}