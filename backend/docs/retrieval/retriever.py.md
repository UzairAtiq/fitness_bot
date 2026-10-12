# `retriever.py` Documentation

### 1. Purpose
Encodes user search queries into dense vector embeddings and queries Qdrant Cloud to retrieve the top candidate document chunks.

### 2. What It Does
- `retrieve(query: str, top_k: int = 5)`: Encodes `query` using `sentence-transformers/all-MiniLM-L6-v2`, queries the Qdrant Cloud collection, and returns the top 5 `ScoredPoint` instances with payloads.

### 3. Depends on / Used by
- **Depends on**: `sentence_transformers.SentenceTransformer`, `qdrant_client.QdrantClient`, `app.config.QDRANT_URL`, `app.config.QDRANT_API_KEY`, `app.config.collection_name`.
- **Used by**: `app.pipeline.pipeline` and `tests/benchmark_pipeline.py`.

### 4. How to Modify
1. To change the default candidate pool size, modify the default `top_k` parameter in `retrieve(query, top_k=5)`.
2. To add vector search filters (e.g., filtering by `doc_id` or specific chapters), pass a `Filter` object into `client.query_points(query_filter=...)`.
3. Test retrieval performance and recall by running `python backend/tests/benchmark_pipeline.py --profile-only`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: First-stage vector retrieval, query embedding transformations, and Qdrant search filters.
- **Do NOT add here**: Cross-encoder reranking logic (which belongs in `reranker.py`) or prompt building.
