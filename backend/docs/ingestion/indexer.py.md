# `indexer.py` Documentation

### 1. Purpose
Computes dense vector embeddings from chunked text and indexes points into a Qdrant collection with deterministic UUIDs.

### 2. What It Does
- `indexer(chunked_text, name, book_id)`: Initializes QdrantClient, creates the collection with 384-dim cosine distance if missing, computes embeddings via `sentence-transformers/all-MiniLM-L6-v2`, creates UUID5 points with text/header payload, and upserts them.

### 3. Depends on / Used by
- **Depends on**: `sentence_transformers.SentenceTransformer`, `qdrant_client.QdrantClient`, `app.config.QDRANT_URL`, `app.config.QDRANT_API_KEY`, `uuid.uuid5`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To change vector dimensionality or embedding model, update `SentenceTransformer(...)` model ID and the `VectorParams(size=...)` setting.
2. To add additional metadata to Qdrant payloads (e.g., exercise category, page number), add keys to the `payload` dictionary inside `PointStruct`.
3. To batch upserts for massive datasets, wrap points in chunk batches (e.g. 100 points per `client.upsert`).

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Embedding generation, vector database schema configuration, and batch upsert logic.
- **Do NOT add here**: Query retrieval functions (which belong in `retriever.py`) or text splitting algorithms.
