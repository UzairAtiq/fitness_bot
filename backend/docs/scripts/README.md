# Scripts Package Documentation

### Purpose
Contains command-line automation scripts for batch indexing raw course literature into Qdrant Cloud and running qualitative evaluation benchmarks across sample questions.

### File List
- **[ingest.py](ingest.py.md)**: Loads source documents, cleans formatting, splits text, embeds chunks, and uploads points to Qdrant Cloud.
- **[evaluate.py](evaluate.py.md)**: Runs 8 sample questions from different chapters of the source book through the pipeline and records answers.

### Import Rules
- **Can Import**: `app.ingestion`, `app.pipeline`, and `app.config`.
- **Cannot Be Imported By**: Internal library packages (`app.*`). Scripts are standalone CLI entry points.

### Where New Code Goes
- **New Data Ingestion Pipelines**: Add new ingestion tasks to `scripts/ingest.py` or new dedicated scripts in `scripts/`.
- **Automated Verification / Evaluation Utilities**: Add new benchmark runners to `scripts/`.
- **Database Maintenance / Migration Scripts**: Add dedicated maintenance scripts inside `scripts/`.
