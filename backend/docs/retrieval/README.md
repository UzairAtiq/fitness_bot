# Retrieval Package Documentation

### Purpose
Implements the multi-stage document retrieval system: initial dense vector similarity retrieval against Qdrant Cloud followed by high-precision cross-encoder reranking.

### File List
- **[retriever.py](retriever.py.md)**: Encodes search queries and fetches top-k candidate chunks from Qdrant Cloud.
- **[reranker.py](reranker.py.md)**: Scores candidate query-document pairs using a cross-encoder model to return the top 2 most relevant passages.

### Import Rules
- **Can Import**: `app.config`.
- **Cannot Import**: Higher layers (`app.pipeline` or `app.api`).
- **Imported By**: `app.pipeline`.

### Where New Code Goes
- **Query Preprocessing / Embedding Tweaks**: Add to `app/retrieval/retriever.py`.
- **Hybrid Retrieval (Dense + Sparse/BM25)**: Implement sparse retrieval helpers inside `app/retrieval/` and integrate into `retriever.py`.
- **Alternative Cross-Encoders or Reciprocal Rank Fusion (RRF)**: Add to `app/retrieval/reranker.py`.
