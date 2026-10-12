# Scripts Documentation

### Purpose
Contains command-line automation scripts for batch indexing raw course literature into Qdrant Cloud and running qualitative evaluation benchmarks across sample questions.

### Import Rules
- **Can Import**: `app.ingestion`, `app.pipeline`, and `app.config`.
- **Cannot Be Imported By**: Internal library packages (`app.*`). Scripts are standalone CLI entry points.

### Where New Code Goes
- **New Data Ingestion Pipelines**: Add new ingestion tasks to `scripts/ingest.py` or new dedicated scripts in `scripts/`.
- **Automated Verification / Evaluation Utilities**: Add new benchmark runners to `scripts/`.
- **Database Maintenance / Migration Scripts**: Add dedicated maintenance scripts inside `scripts/`.

---

## Module Reference: `ingest.py`

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

---

## Module Reference: `evaluate.py`

### 1. Purpose
Runs qualitative evaluation across 8 benchmark bodybuilding questions and serializes generated answers and retrieved chunk metadata to disk.

### 2. What It Does
- `questions`: List of 8 curated domain test questions covering workout volume, exercise form, and anatomy.
- `run_evaluation()`: Iterates over benchmark questions, calls `pipeline(question, debug=True)`, pauses for API rate limits, and writes results to `backend/data/evaluation/evaluate.json`.

### 3. Depends on / Used by
- **Depends on**: `app.pipeline.pipeline`, `pathlib.Path`, `json`, `time`.
- **Used by**: Automated evaluation suites and developers running `python backend/scripts/evaluate.py`.

### 4. How to Modify
1. To add new benchmark questions, append question strings to the `questions` list in `evaluate.py`.
2. To modify rate-limit pause intervals between requests, adjust `time.sleep(...)` inside `run_evaluation`.
3. Run the evaluation script: `python backend/scripts/evaluate.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Domain question evaluation suites, output serialization, and evaluation metrics logging.
- **Do NOT add here**: Low-level database initialization or web server route definitions.
