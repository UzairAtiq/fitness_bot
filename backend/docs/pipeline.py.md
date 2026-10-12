# `pipeline.py` Documentation

### 1. Purpose
Coordinates the complete end-to-end question answering workflow connecting retrieval, reranking, prompt building, and LLM inference.

### 2. What It Does
- `pipeline(query: str, debug: bool = False)`: Retrieves candidate document chunks, reranks them with cross-encoder scoring, builds the guarded prompt, sends it to the LLM, and optionally returns chunk metadata in debug mode.

### 3. Depends on / Used by
- **Depends on**: `app.retrieval.retriever.retrieve`, `app.retrieval.reranker.reranker`, `app.generation.prompt.build_prompt`, `app.generation.llm.send_prompt`.
- **Used by**: `app.api.routes.ask` and `scripts/evaluate.py`.

### 4. How to Modify
1. To change the number of chunks passed through, adjust retrieval or reranker parameters.
2. To add an extra pipeline step (e.g., query rewriting or answer validation), invoke the new module between retrieval and generation.
3. Test pipeline execution by running `backend/tests/benchmark_pipeline.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Workflow orchestrations and sequence logic tying components together.
- **Do NOT add here**: Low-level database client queries, raw SQL/Qdrant payloads, or FastAPI HTTP endpoints.
