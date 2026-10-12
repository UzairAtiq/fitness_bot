# `test_pipeline.py` Documentation

### 1. Purpose
Contains integration tests verifying end-to-end question answering pipeline flow and error handling.

### 2. What It Does
- Test module: Tests integration across retrieval, reranking, and generation modules, checking answer outputs and debug payload structures.

### 3. Depends on / Used by
- **Depends on**: `pytest`, `app.pipeline.pipeline`.
- **Used by**: Pytest test suite (`pytest backend/tests/test_pipeline.py`).

### 4. How to Modify
1. Create integration test cases asserting pipeline behavior on sample test questions.
2. Use mocking (`unittest.mock.patch`) to mock external network calls to Qdrant or Groq when running in offline CI environments.
3. Execute tests using `pytest backend/tests/test_pipeline.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Integration tests for pipeline execution, debug return formats, and error recovery.
- **Do NOT add here**: Frontend UI assertions or database schema migrations.
