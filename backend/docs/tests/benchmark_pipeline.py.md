# `benchmark_pipeline.py` Documentation

### 1. Purpose
Profiles CPU and memory usage while timing individual latencies across embedding, vector search, reranking, prompt building, and LLM generation.

### 2. What It Does
- `get_system_resources()`: Reads CPU core counts, RAM capacity, available RAM, and swap memory usage.
- `benchmark_single_run(...)`: Times each pipeline step for a test query and returns latency metrics and answer previews.
- `print_report(...)`: Prints a structured terminal table displaying latencies, percentage shares, and bottleneck flags.
- `diagnose_bottlenecks(...)`: Diagnoses causes of pipeline delays (e.g., cross-encoder CPU saturation, Groq rate limits).
- `main()`: Parses CLI arguments (`--runs`, `--query`, `--no-system-check`, `--profile-only`) and executes benchmarks.

### 3. Depends on / Used by
- **Depends on**: `sentence_transformers`, `qdrant_client`, `langchain_groq`, `app.config`, `app.generation.prompt`.
- **Used by**: Developers profiling latency bottlenecks via `python backend/tests/benchmark_pipeline.py`.

### 4. How to Modify
1. To benchmark a new query or change default runs, use flags: `python backend/tests/benchmark_pipeline.py --runs 5 --query "How to squat?"`.
2. To test only local vector stages without spending Groq API tokens, run with `--profile-only`.
3. To add a new pipeline step into timing measurements, add a timed block in `benchmark_single_run`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Profiling harnesses, hardware metric collectors, latency timers, and bottleneck diagnostic rules.
- **Do NOT add here**: Production business logic or web server endpoints.
