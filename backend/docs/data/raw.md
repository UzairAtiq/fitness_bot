# `data/raw` Documentation

### 1. Purpose
Stores the original, un-chunked reference markdown text of the Joe Weider Bodybuilding System training course.

### 2. What It Does
- Knowledge asset: Supplies the domain text containing training routines, biomechanics explanations, anatomy guides, and exercise charts.

### 3. Depends on / Used by
- **Depends on**: Source course markdown document (`joe-weider-s-bodybuilding-system-joe-weider-2929.md`).
- **Used by**: `app/ingestion/loaders.py` and `scripts/ingest.py`.

### 4. How to Modify
1. To add more course books or manuals, save the raw markdown file into `backend/data/raw/`.
2. Update the filename reference in `backend/scripts/ingest.py`.
3. Re-run ingestion: `python backend/scripts/ingest.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Ground truth markdown books, training textbooks, and curriculum documents.
- **Do NOT add here**: Serialized JSON outputs or vector database cache files.
