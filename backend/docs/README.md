# Backend Documentation Index

Overview of all backend architectural components, subsystems, files, and maintenance guides.

---

## Component Documentation

- **[API Documentation](api.md)**: FastAPI endpoints, middleware, authentication, and request handling.
- **[Generation Documentation](generation.md)**: Prompt construction and Groq LLM inference handlers.
- **[Ingestion Documentation](ingestion.md)**: Document loading, cleaning, chunking, and Qdrant vector indexing.
- **[Retrieval Documentation](retrieval.md)**: Dense vector similarity retrieval and cross-encoder reranking.
- **[Scripts Documentation](scripts.md)**: Ingestion and qualitative evaluation automation scripts.
- **[Tests Documentation](tests.md)**: Latency benchmarks and pipeline test suites.
- **[Data Documentation](data.md)**: Raw source markdown books and persisted evaluation outputs.

---

## Core Backend Files

- **[pipeline.py](pipeline.py.md)**: End-to-end question answering pipeline orchestration connecting retrieval, reranking, and generation.
- **config.py**: Loads environment variables from `.env` using `python-dotenv` and defines global system constants (`QDRANT_URL`, `collection_name`, `GROQ_API_KEY`, `SHARED_ACCESS_KEY`).
- **requirements.txt**: Pinned Python runtime dependencies for FastAPI, Qdrant client, sentence-transformers, PyTorch, and Groq.
- **.env.example**: Template specifying required and optional environment variable keys for service configuration.
