# Data Documentation

### Purpose
Stores raw knowledge base literature (Markdown books) and output datasets from benchmark evaluation runs.

### Import Rules
- **Can Import**: None. Data files are static assets.
- **Used By**: `app.ingestion.loaders`, `scripts/ingest.py`, and `scripts/evaluate.py`.

### Where New Code Goes
- **New Training Textbooks / Reference Courses**: Place markdown source files in `data/raw/`.
- **New Evaluation Outputs / Metric Logs**: Written to `data/evaluation/`.

---

## Directory Reference: `data/raw`

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

---

## File Reference: `evaluate.json`

### 1. Purpose
Stores recorded benchmark evaluation outputs containing questions, generated responses, and retrieved context chunks with similarity scores.

### 2. What It Does
- JSON dataset: Stores an array of records where each entry contains `question`, `answer`, and `retrieved_chunks` (with headers, scores, and book IDs).

### 3. Depends on / Used by
- **Depends on**: Output from `scripts/evaluate.py`.
- **Used by**: Developers and researchers inspecting retrieval relevance and LLM grounding fidelity.

### 4. How to Modify
1. To regenerate the file, execute `python backend/scripts/evaluate.py`.
2. Do not manually edit the file unless correcting corrupted test records.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Automated evaluation outputs produced by benchmark test suites.
- **Do NOT add here**: Raw training documents or source markdown files.
