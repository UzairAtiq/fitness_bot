# `reranker.py` Documentation

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
