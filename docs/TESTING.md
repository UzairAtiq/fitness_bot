# Testing and Profiling

## 1. Latency and Resource Profiling

A benchmark script is included in `tests/benchmark_pipeline.py` to measure latency across each step (MiniLM embeddings, Qdrant vector search, CrossEncoder reranking, Groq LLM call) and check CPU/RAM usage:

```bash
python tests/benchmark_pipeline.py --runs 3
```

### Useful Flags
- `--runs <int>`: Number of runs to average (default: 3).
- `--query "<text>"`: Custom question to test.
- `--no-system-check`: Skips reading system CPU and RAM stats.
- `--profile-only`: Measures step timings without generating full text answers.

---

## 2. Qualitative Retrieval Evaluation

Runs 8 sample questions from different chapters of the source book through the pipeline:

```bash
python scripts/evaluate.py
```

Outputs are written to `data/evaluation/evaluate.json`, including the question, answer, and retrieved chunk headers with scores.

---

## 3. Unit Tests

> Note: Unit test files in `tests/` currently contain stubs only. Full automated test coverage for chunking, retrieval scoring, and error handling is planned.
