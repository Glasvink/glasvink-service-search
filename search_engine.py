from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

documents = [
    "Wij repareren gebarsten of kapot raamglas in bestaande ramen.",
    "Wij vervangen gebroken ruiten in bestaande ramen en deuren.",
    "Wij leveren en plaatsen HR++ dubbel glas om warmteverlies via ramen te beperken.",
    "Wij leveren en plaatsen vacuümglas voor betere isolatie en minder warmteverlies.",
    "Wij leveren en plaatsen kunststof kozijnen voor woningen en bedrijfspanden.",
    "Wij leveren en plaatsen kunststof voordeuren en achterdeuren.",
    "Wij leveren en plaatsen nieuwe kunststof schuifpuien voor woningen. Een kunststof schuifpui is een schuifdeur naar de tuin of het terras.",
    "Wij repareren en restaureren oude glas-in-loodramen.",
    "Wij leveren en plaatsen veiligheidsglas voor woningen en bedrijven.",
    "Wij verminderen geluid van buiten met isolatieglas."
]

document_embeddings = model.encode(
    documents,
    convert_to_tensor=True
)


def semantic_search(query, top_k=3, threshold=0.50):
    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    similarities = util.cos_sim(
        query_embedding,
        document_embeddings
    )[0]

    top_results = similarities.topk(
        min(top_k, len(documents))
    )

    results = []

    for score, index in zip(
        top_results.values,
        top_results.indices
    ):
        similarity = score.item()

        if similarity >= threshold:
            results.append({
                "score": similarity,
                "document": documents[index.item()]
            })

    return results
