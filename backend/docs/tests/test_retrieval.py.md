# `test_retrieval.py` Documentation

### 1. Purpose
Contains unit test cases for vector similarity retrieval querying and cross-encoder reranker scoring logic.

### 2. What It Does
- Test module: Validates that candidate points are correctly scored, sorted in descending order, and filtered to the top-k passages.

### 3. Depends on / Used by
- **Depends on**: `pytest`, `app.retrieval.retriever`, `app.retrieval.reranker`.
- **Used by**: Pytest test suite (`pytest backend/tests/test_retrieval.py`).

### 4. How to Modify
1. Add test functions testing cross-encoder reranking ordering with dummy chunks and known query pairs.
2. Add tests verifying character truncation and point selection in `reranker`.
3. Execute tests using `pytest backend/tests/test_retrieval.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Unit tests for retrieval filters, embedding vector shapes, and reranker sorting logic.
- **Do NOT add here**: Raw training scripts or full LLM evaluation prompts.
