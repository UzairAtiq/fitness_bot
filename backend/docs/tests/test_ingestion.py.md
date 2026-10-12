# `test_ingestion.py` Documentation

### 1. Purpose
Contains unit test specifications and test cases for text cleaning, normalization, and markdown header chunking.

### 2. What It Does
- Test module: Verifies that `clean_text` removes page markers and irregular whitespace, and that `chunk_document` attaches correct header metadata.

### 3. Depends on / Used by
- **Depends on**: `pytest`, `app.ingestion.cleaner`, `app.ingestion.chunker`.
- **Used by**: Pytest test runner (`pytest backend/tests/test_ingestion.py`).

### 4. How to Modify
1. Define test functions prefixed with `test_` (e.g., `def test_clean_text_removes_page_markers(): ...`).
2. Add assertions comparing cleaned text or chunk structures to expected outputs.
3. Run tests using `pytest backend/tests/`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Unit tests for text normalization, chunk splitting edge cases, and header hierarchy parsing.
- **Do NOT add here**: Network calls to live Qdrant clusters or LLM APIs.
