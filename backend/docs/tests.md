# Tests Documentation

### Purpose
Contains performance benchmarking scripts, latency profilers, and automated unit/integration test suites for the backend.

### Import Rules
- **Can Import**: `app.*` and `scripts.*`.
- **Cannot Be Imported By**: Application production code (`app.*`). Tests are external verifiers.

### Where New Code Goes
- **Unit Tests for Chunking / Ingestion**: Add test cases to `tests/test_ingestion.py`.
- **Unit Tests for Vector Retrieval / Scoring**: Add test cases to `tests/test_retrieval.py`.
- **End-to-End Pipeline Tests**: Add test cases to `tests/test_pipeline.py`.
- **Performance Profiling Tools**: Add profilers or benchmark flags to `tests/benchmark_pipeline.py`.

---

## Module Reference: `benchmark_pipeline.py`

### 1. Purpose
Profiles CPU and memory usage while timing individual latencies across embedding, vector search, reranking, prompt building, and LLM generation.

### 2. What It Does
- `get_system_resources()`: Reads CPU core counts, RAM capacity, available RAM, and swap memory usage.
- `benchmark_single_run(...)`: Times each pipeline step for a test query and returns latency metrics and answer previews.
- `print_report(...)`: Prints a structured terminal table displaying latencies, percentage shares, and bottleneck flags.
- `diagnose_bottlenecks(...)`: Diagnoses causes of pipeline delays (e.g., cross-encoder CPU saturation, Groq rate limits).
- `main()`: Parses CLI arguments (`--runs`, `--query`, `--no-system-check`, `--profile-only`) and executes benchmarks.

### 3. Depends on / Used by
- **Depends on**: `sentence_transformers`, `qdrant_client`, `langchain_groq`, `app.config`, `app.generation.prompt`.
- **Used by**: Developers profiling latency bottlenecks via `python backend/tests/benchmark_pipeline.py`.

### 4. How to Modify
1. To benchmark a new query or change default runs, use flags: `python backend/tests/benchmark_pipeline.py --runs 5 --query "How to squat?"`.
2. To test only local vector stages without spending Groq API tokens, run with `--profile-only`.
3. To add a new pipeline step into timing measurements, add a timed block in `benchmark_single_run`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Profiling harnesses, hardware metric collectors, latency timers, and bottleneck diagnostic rules.
- **Do NOT add here**: Production business logic or web server endpoints.

---

## Module Reference: `test_ingestion.py`

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

---

## Module Reference: `test_retrieval.py`

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

---

## Module Reference: `test_pipeline.py`

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
