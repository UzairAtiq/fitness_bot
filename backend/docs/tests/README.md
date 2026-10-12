# Tests Package Documentation

### Purpose
Contains performance benchmarking scripts, latency profilers, and automated unit/integration test suites for the backend.

### File List
- **[benchmark_pipeline.py](benchmark_pipeline.py.md)**: Profiles CPU/RAM usage and breaks down latencies across embedding, vector search, reranking, and generation.
- **[test_ingestion.py](test_ingestion.py.md)**: Unit tests for text cleaning and markdown header chunking.
- **[test_retrieval.py](test_retrieval.py.md)**: Unit tests for vector retrieval and cross-encoder scoring.
- **[test_pipeline.py](test_pipeline.py.md)**: Integration tests verifying complete end-to-end question answering pipeline.

### Import Rules
- **Can Import**: `app.*` and `scripts.*`.
- **Cannot Be Imported By**: Application production code (`app.*`). Tests are external verifiers.

### Where New Code Goes
- **Unit Tests for Chunking / Ingestion**: Add test cases to `tests/test_ingestion.py`.
- **Unit Tests for Vector Retrieval / Scoring**: Add test cases to `tests/test_retrieval.py`.
- **End-to-End Pipeline Tests**: Add test cases to `tests/test_pipeline.py`.
- **Performance Profiling Tools**: Add profilers or benchmark flags to `tests/benchmark_pipeline.py`.
