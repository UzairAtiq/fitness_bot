# Backend Documentation Index

Overview of all backend architectural components, subpackages, files, and maintenance guides.

---

## Documentation Folders

- **[API Documentation](api/README.md)**: FastAPI endpoints, middleware, authentication, and request handling.
- **[Generation Documentation](generation/README.md)**: Prompt construction and Groq LLM inference handlers.
- **[Ingestion Documentation](ingestion/README.md)**: Document loading, cleaning, chunking, and Qdrant vector indexing.
- **[Retrieval Documentation](retrieval/README.md)**: Dense vector similarity retrieval and cross-encoder reranking.
- **[Scripts Documentation](scripts/README.md)**: Ingestion and qualitative evaluation automation scripts.
- **[Tests Documentation](tests/README.md)**: Latency benchmarks and pipeline test suites.
- **[Data Documentation](data/README.md)**: Raw source markdown books and persisted evaluation outputs.

---

## Core Backend Files

- **[config.py](config.py.md)**: Environment variable loading and global system configuration.
- **[pipeline.py](pipeline.py.md)**: End-to-end question answering pipeline orchestration.
- **[.env.example](.env.example.md)**: Environment variables template and setup reference.
- **[requirements.txt](requirements.txt.md)**: Python dependencies and versions.
