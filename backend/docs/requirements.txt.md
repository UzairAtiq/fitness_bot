# `requirements.txt` Documentation

### 1. Purpose
Declares pinned Python package dependencies and version specifications for the backend runtime and RAG pipeline.

### 2. What It Does
- Package list: Pins libraries including `fastapi`, `uvicorn`, `qdrant-client`, `sentence-transformers`, `torch`, `langchain-core`, `langchain-groq`, and `python-dotenv`.

### 3. Depends on / Used by
- **Depends on**: Python package ecosystem and PyPI / PyTorch CPU wheels.
- **Used by**: Virtual environments (`pip install -r backend/requirements.txt`) and `docker/Dockerfile`.

### 4. How to Modify
1. Install a new dependency in your virtual environment: `pip install <package>`.
2. Inspect or pin the specific version inside `backend/requirements.txt`.
3. Verify compatibility by running `python -c "import <package>"` and executing `backend/tests/benchmark_pipeline.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Necessary runtime dependencies for the backend API, embeddings, and database drivers.
- **Do NOT add here**: Frontend dependencies (which belong in `frontend/package.json`) or transient build artifacts.
