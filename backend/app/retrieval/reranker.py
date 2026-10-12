"""Cross-encoder reranking module for prioritizing top retrieved chunks."""
from sentence_transformers import CrossEncoder

# initialize lightweight cpu-optimized cross-encoder
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2", max_length=384)


def reranker(query: str, chunks: list) -> list:
    """Scores candidate chunks against the query using a cross-encoder model.

    Steps:
        1. Create query-text pairs truncating chunk text to 1,200 characters for CPU efficiency.
        2. Run cross-encoder model prediction across all pairs to compute relevance scores.
        3. Sort the chunks in descending order of cross-encoder prediction scores.
        4. Truncate and return the top 2 highest-scoring chunks.

    Args:
        query: User query string.
        chunks: List of retrieved Qdrant ScoredPoint objects with text payload.

    Returns:
        List containing the top 2 ranked Qdrant points.

    Raises:
        None.
    """
    print("Reranking chunks with CPU-optimized cross-encoder")

    # score relevance using first 1200 characters while keeping full text in chunk payload
    pairs = [(query, chunk.payload.get("text", "")[:1200]) for chunk in chunks]

    # predict ranking scores
    scores = model.predict(pairs)

    # sort chunks from highest to lowest score
    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True,
    )

    # return top 2 most relevant chunks
    return [chunk for chunk, score in ranked[:2]]

