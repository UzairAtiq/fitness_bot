# `ingest.py` Documentation

### 1. Purpose
Executes the batch ingestion workflow that loads the raw source book from disk, cleans formatting, chunks into headers, embeds, and uploads points to Qdrant Cloud.

### 2. What It Does
- `run_ingest()`: Resolves book path, reads raw markdown, runs `clean_text()`, splits into header chunks via `chunk_document()`, and upserts to Qdrant using `indexer()`.

### 3. Depends on / Used by
- **Depends on**: `app.ingestion.loaders`, `app.ingestion.cleaner`, `app.ingestion.chunker`, `app.ingestion.indexer`, `app.config.collection_name`.
- **Used by**: Developers and CI/CD jobs executing `python backend/scripts/ingest.py`.

### 4. How to Modify
1. To ingest additional books or documents, define additional file paths and book identifiers and call `indexer(...)` for each.
2. To ingest into an alternative Qdrant collection, set `collection_name` in `backend/.env`.
3. Run the script: `python backend/scripts/ingest.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Batch document processing scripts and collection seeding routines.
- **Do NOT add here**: FastAPI endpoint logic or frontend service callers.
