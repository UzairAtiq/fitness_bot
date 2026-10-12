# Ingestion Package Documentation

### Purpose
Handles the data ingestion lifecycle: loading raw markdown books, normalizing formatting and page markers, splitting text into structured chunks by header hierarchy, and indexing vectors into Qdrant Cloud.

### File List
- **[loaders.py](loaders.py.md)**: Reads and loads raw source text files from disk.
- **[cleaner.py](cleaner.py.md)**: Cleans page numbers, form-feeds, and erratic whitespace from markdown text.
- **[chunker.py](chunker.py.md)**: Splits cleaned markdown text into chunks using header boundaries (H1 to H4).
- **[indexer.py](indexer.py.md)**: Computes dense vector embeddings and upserts point structures into Qdrant.

### Import Rules
- **Can Import**: `app.config`.
- **Cannot Import**: Higher layers (`app.pipeline` or `app.api`).
- **Imported By**: `scripts/ingest.py`.

### Where New Code Goes
- **New Document File Formats (PDF, EPUB)**: Add loader functions in `app/ingestion/loaders.py`.
- **Custom Text Sanitization / Regex Rules**: Add to `app/ingestion/cleaner.py`.
- **Alternative Splitting Strategies (semantic splitting, recursive splitting)**: Add to `app/ingestion/chunker.py`.
- **Alternative Vector DB Destinations or Vector Configs**: Add to `app/ingestion/indexer.py`.
