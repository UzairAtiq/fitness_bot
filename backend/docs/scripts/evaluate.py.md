# `evaluate.py` Documentation

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
