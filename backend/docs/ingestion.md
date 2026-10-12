# Ingestion Documentation

### Purpose
Handles the data ingestion lifecycle: loading raw markdown books, normalizing formatting and page markers, splitting text into structured chunks by header hierarchy, and indexing vectors into Qdrant Cloud.

### Import Rules
- **Can Import**: `app.config`.
- **Cannot Import**: Higher layers (`app.pipeline` or `app.api`).
- **Imported By**: `scripts/ingest.py`.

### Where New Code Goes
- **New Document File Formats (PDF, EPUB)**: Add loader functions in `app/ingestion/loaders.py`.
- **Custom Text Sanitization / Regex Rules**: Add to `app/ingestion/cleaner.py`.
- **Alternative Splitting Strategies (semantic splitting, recursive splitting)**: Add to `app/ingestion/chunker.py`.
- **Alternative Vector DB Destinations or Vector Configs**: Add to `app/ingestion/indexer.py`.

---

## Module Reference: `loaders.py`

### 1. Purpose
Reads raw text files from the local filesystem with UTF-8 encoding.

### 2. What It Does
- `load_book(path: str)`: Opens a file path in UTF-8 read mode and returns the complete text content as a string.

### 3. Depends on / Used by
- **Depends on**: Python standard library `open`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To support additional file encodings or error handlers, pass parameters into `open()` inside `load_book`.
2. To support directory traversal or multiple file loading, add a `load_directory(dir_path)` function.
3. Test loading by executing `python -c "from app.ingestion.loaders import load_book; print(len(load_book('backend/data/raw/joe-weider-s-bodybuilding-system-joe-weider-2929.md')))"`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: File I/O readers for raw documents (text, markdown, PDF).
- **Do NOT add here**: Text cleaning logic (which belongs in `cleaner.py`) or chunk splitting logic.

---

## Module Reference: `cleaner.py`

### 1. Purpose
Normalizes text, strips OCR/PDF conversion artifacts, removes page markers, and collapses excessive whitespace.

### 2. What It Does
- `clean_text(text: str)`: Removes form-feed characters, strips `[PAGE N]` and standalone page numbers, normalizes Windows line endings, cleans trailing spaces, and standardizes markdown header spacing.

### 3. Depends on / Used by
- **Depends on**: Python standard library `re`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To strip new artifact patterns (e.g. copyright notices or headers), add a regex pattern using `re.sub(pattern, replacement, text)`.
2. Ensure new regex patterns do not inadvertently strip meaningful exercise tables or markdown syntax.
3. Test by running `clean_text` on sample text strings.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Regex normalization, string sanitizers, character encoding cleansers, and whitespace formatters.
- **Do NOT add here**: File loading logic or vector database operations.

---

## Module Reference: `chunker.py`

### 1. Purpose
Splits cleaned markdown text into document chunks while preserving heading hierarchy (H1 through H4) in metadata.

### 2. What It Does
- `chunk_document(cleaned_text: str)`: Configures `MarkdownHeaderTextSplitter` with `#`, `##`, `###`, and `####` headers, and splits text into structured LangChain `Document` chunks.

### 3. Depends on / Used by
- **Depends on**: `langchain_text_splitters.MarkdownHeaderTextSplitter`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To change the headers split on or add deeper levels (e.g., `#####`), edit `headers_to_split_on`.
2. To apply a character-level secondary split for extra-long sections, chain `RecursiveCharacterTextSplitter` after the markdown header split.
3. Test chunking by verifying chunk counts and metadata headers on sample texts.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Document chunking, text splitting, token count estimators, and chunk boundary algorithms.
- **Do NOT add here**: Text cleaning regex (which belongs in `cleaner.py`) or embedding computations.

---

## Module Reference: `indexer.py`

### 1. Purpose
Computes dense vector embeddings from chunked text and indexes points into a Qdrant collection with deterministic UUIDs.

### 2. What It Does
- `indexer(chunked_text, name, book_id)`: Initializes QdrantClient, creates the collection with 384-dim cosine distance if missing, computes embeddings via `sentence-transformers/all-MiniLM-L6-v2`, creates UUID5 points with text/header payload, and upserts them.

### 3. Depends on / Used by
- **Depends on**: `sentence_transformers.SentenceTransformer`, `qdrant_client.QdrantClient`, `app.config.QDRANT_URL`, `app.config.QDRANT_API_KEY`, `uuid.uuid5`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To change vector dimensionality or embedding model, update `SentenceTransformer(...)` model ID and the `VectorParams(size=...)` setting.
2. To add additional metadata to Qdrant payloads (e.g., exercise category, page number), add keys to the `payload` dictionary inside `PointStruct`.
3. To batch upserts for massive datasets, wrap points in chunk batches (e.g. 100 points per `client.upsert`).

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Embedding generation, vector database schema configuration, and batch upsert logic.
- **Do NOT add here**: Query retrieval functions (which belong in `retriever.py`) or text splitting algorithms.
