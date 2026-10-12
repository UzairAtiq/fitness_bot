# `config.py` Documentation

### 1. Purpose
Loads environment variables from local configuration files and exposes configuration constants across the backend.

### 2. What It Does
- `load_dotenv()`: Detects and loads `.env` files located in either the `backend/` directory or project root.
- Module-level constants: Exports `QDRANT_URL`, `collection_name`, `QDRANT_API_KEY`, `GROQ_API_KEY`, `GROK_API_KEY`, and `SHARED_ACCESS_KEY`.

### 3. Depends on / Used by
- **Depends on**: `os`, `pathlib.Path`, `python-dotenv`.
- **Used by**: `app/api/routes.py`, `app/generation/llm.py`, `app/ingestion/indexer.py`, `app/retrieval/retriever.py`, and `scripts/ingest.py`.

### 4. How to Modify
1. Define any new required environment variable in `backend/.env.example`.
2. In `app/config.py`, read the variable using `os.getenv("VARIABLE_NAME", default_value)`.
3. Export the constant and import it into whichever module requires it.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Simple string, integer, or boolean environment configurations and connection URLs.
- **Do NOT add here**: Stateful database connection clients, complex business logic, or runtime API routes.
