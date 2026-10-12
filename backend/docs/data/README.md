# Data Package Documentation

### Purpose
Stores raw knowledge base literature (Markdown books) and output datasets from benchmark evaluation runs.

### File List
- **[raw.md](raw.md)**: Overview of raw training literature (`data/raw/joe-weider-s-bodybuilding-system-joe-weider-2929.md`).
- **[evaluate.json.md](evaluate.json.md)**: Schema and reference for evaluation benchmark outputs (`data/evaluation/evaluate.json`).

### Import Rules
- **Can Import**: None. Data files are static assets.
- **Used By**: `app.ingestion.loaders`, `scripts/ingest.py`, and `scripts/evaluate.py`.

### Where New Code Goes
- **New Training Textbooks / Reference Courses**: Place markdown source files in `data/raw/`.
- **New Evaluation Outputs / Metric Logs**: Written to `data/evaluation/`.
