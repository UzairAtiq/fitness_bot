"""Generates dense embeddings and upserts document chunks into Qdrant."""
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from app.config import QDRANT_URL, QDRANT_API_KEY
from uuid import uuid5, NAMESPACE_DNS

def indexer(chunked_text, name, book_id):
    """Embeds document chunks and uploads vector points to a Qdrant collection.

    Steps:
        1. Initialize QdrantClient with configured cloud URL and API key.
        2. Verify if collection exists, creating it with 384-dim cosine distance if not.
        3. Load SentenceTransformer all-MiniLM-L6-v2 model.
        4. Iterate over chunks, extracting content and hierarchical header metadata.
        5. Generate dense vector embeddings for each chunk text.
        6. Construct PointStruct instances with deterministic UUID5 identifiers and payloads.
        7. Upsert batch of points into the Qdrant collection.

    Args:
        chunked_text: Iterable of LangChain Document objects containing text and headers.
        name: Target Qdrant collection name string.
        book_id: Unique identifier string for the document source.

    Returns:
        None.

    Raises:
        Exception: If connecting to Qdrant or upserting points fails.
    """

    # Setting up Qdrant client
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        cloud_inference=True,
    )

    # Creating Qdrant collection if it does not exist
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

    # Loading pretrained model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Points list for qdrant
    points = []
    for i, chunk in enumerate(chunked_text):
        # loading the metadata and page content from langchain document object
        page_content = chunk.page_content

        # Getting and Joining all existing headers in hierarchical order
        levels = [chunk.metadata.get(f"Header {n}") for n in range(1, 5)]
        header = " > ".join(h for h in levels if h)

        # calculate embeddings for chunks
        emebeddings = model.encode(page_content)

        # Adding the chunks and headers to a list using pointstruct
        points.append(
            PointStruct(
                id=str(uuid5(NAMESPACE_DNS, f"{book_id}_{i}")),
                vector=emebeddings.tolist(),
                payload={"text": page_content, "header": header, "doc_id": book_id},
            )
        )

    # Sending to qdrant
    client.upsert(collection_name=name, points=points)



