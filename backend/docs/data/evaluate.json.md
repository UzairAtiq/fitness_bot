# `evaluate.json` Documentation

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
