# Retrieval Documentation

### Purpose
Implements the multi-stage document retrieval system: initial dense vector similarity retrieval against Qdrant Cloud followed by high-precision cross-encoder reranking.

### Import Rules
- **Can Import**: `app.config`.
- **Cannot Import**: Higher layers (`app.pipeline` or `app.api`).
- **Imported By**: `app.pipeline`.

### Where New Code Goes
- **Query Preprocessing / Embedding Tweaks**: Add to `app/retrieval/retriever.py`.
- **Hybrid Retrieval (Dense + Sparse/BM25)**: Implement sparse retrieval helpers inside `app/retrieval/` and integrate into `retriever.py`.
- **Alternative Cross-Encoders or Reciprocal Rank Fusion (RRF)**: Add to `app/retrieval/reranker.py`.

---

## Module Reference: `retriever.py`

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

---

## Module Reference: `reranker.py`

### 1. Purpose
Applies a lightweight, CPU-optimized cross-encoder model to score and rerank candidate chunks, selecting the top 2 most relevant passages for LLM context.

### 2. What It Does
- `model`: Instantiates `cross-encoder/ms-marco-MiniLM-L-6-v2` with `max_length=384`.
- `reranker(query: str, chunks: list)`: Truncates candidate chunk text to 1,200 characters, predicts cross-encoder relevance scores, sorts candidates descending, and returns the top 2 chunks.

### 3. Depends on / Used by
- **Depends on**: `sentence_transformers.CrossEncoder`.
- **Used by**: `app.pipeline.pipeline` and `tests/benchmark_pipeline.py`.

### 4. How to Modify
1. To change the number of reranked passages returned, adjust the slice `ranked[:2]` inside `reranker`.
2. To tune character truncation length for CPU speed vs contextual accuracy, modify `[:1200]`.
3. Test reranking inference time by running `python backend/tests/benchmark_pipeline.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Second-stage rerankers, neural cross-encoders, and passage relevance scoring functions.
- **Do NOT add here**: Initial vector database retrieval (which belongs in `retriever.py`) or LLM prompt formatting.
