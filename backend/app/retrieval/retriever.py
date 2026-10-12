"""Retrieves candidate document points from Qdrant vector database."""
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from app.config import QDRANT_URL, QDRANT_API_KEY, collection_name

# initialize qdrant cloud client
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

# initialize sentence transformer embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def retrieve(query: str, top_k: int = 5) -> list:
    """Retrieves top candidate document chunks from Qdrant using vector search.

    Steps:
        1. Encode the input query into a dense vector embedding using all-MiniLM-L6-v2.
        2. Execute vector similarity search against the configured Qdrant collection.
        3. Request full payload attributes for each matched point.
        4. Return the list of matched ScoredPoint instances.

    Args:
        query: User input query text to search.
        top_k: Number of top candidate documents to retrieve (default: 5).

    Returns:
        List of Qdrant ScoredPoint objects containing payload metadata and similarity scores.

    Raises:
        Exception: If network connection to Qdrant Cloud or search query fails.
    """
    print(f"Retrieving chunks from Qdrant Cloud collection: {collection_name}")

    # embed the search query
    query_encoded = model.encode(query)

    # query top matching points from qdrant cloud
    response = client.query_points(
        collection_name=collection_name,
        query=query_encoded,
        with_payload=True,
        limit=top_k,
    ).points

    return response

