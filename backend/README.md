# Backend Overview

The backend is a FastAPI service and Retrieval-Augmented Generation (RAG) engine that answers bodybuilding questions grounded in Joe Weider's training courses using dense vector retrieval, cross-encoder reranking, and Groq LLM inference.

---

## Directory Structure

```text
backend/
├── app/
│   ├── api/
│   │   ├── __init__.py           # API routing package for Fitness Bot
│   │   └── routes.py             # FastAPI REST endpoints (/health, /verify-key, /ask) and CORS
│   ├── generation/
│   │   ├── __init__.py           # Generation package containing LLM client and prompt construction
│   │   ├── llm.py                # ChatGroq client initialization, prompt sending, and rate limit guards
│   │   └── prompt.py             # Domain prompt template with strict bodybuilding guardrails
│   ├── ingestion/
│   │   ├── __init__.py           # Ingestion package containing loading, cleaning, chunking, and indexing
│   │   ├── chunker.py            # Splits markdown text into structured chunks by header hierarchy (H1-H4)
│   │   ├── cleaner.py            # Cleans formatting artifacts and normalizes text from converted markdown
│   │   ├── indexer.py            # Computes dense embeddings and upserts point structures into Qdrant
│   │   └── loaders.py            # Loads raw text from markdown documents on the local filesystem
│   ├── retrieval/
│   │   ├── __init__.py           # Retrieval package containing dense retrieval and cross-encoder reranking
│   │   ├── reranker.py           # Cross-encoder model reranking candidate chunks for relevance
│   │   └── retriever.py          # Qdrant client retrieval function querying top-k candidate chunks
│   ├── __init__.py               # Backend application root package and sys.path resolution
│   ├── config.py                 # Loads environment variables and defines global configuration settings
│   └── pipeline.py               # Coordinates end-to-end RAG pipeline across retrieval, reranking, and generation
├── data/
│   ├── evaluation/
│   │   └── evaluate.json         # Serialized output results from evaluation questions
│   └── raw/
│       └── joe-weider-...md      # Source course text in Markdown format
├── scripts/
│   ├── evaluate.py               # Runs qualitative benchmark questions through the pipeline
│   └── ingest.py                 # Loads, cleans, chunks, embeds, and indexes source documents
├── tests/
│   ├── benchmark_pipeline.py     # Profiles latency and resource consumption across pipeline stages
│   ├── test_ingestion.py         # Unit tests for document cleaning and chunking
│   ├── test_pipeline.py          # Integration tests for end-to-end question answering
│   └── test_retrieval.py         # Unit tests for vector search and reranker scoring
├── .env.example                  # Template defining required environment variables
└── requirements.txt              # Pinned Python package dependencies for backend service
```

---

## Import Rules

To maintain modularity and prevent circular dependencies, adhere to strict architectural layer boundaries:

1. **Hierarchy of Layers**:
   - **Configuration (`app.config`)**: Base layer. Has no dependencies on internal application packages.
   - **Ingestion (`app.ingestion`)** & **Retrieval (`app.retrieval`)**: Standalone data-processing layers. Lower layers must **never** import higher layers (`pipeline` or `api`).
   - **Generation (`app.generation`)**: Standalone prompt and LLM calling layer. Never imports higher layers (`pipeline` or `api`).
   - **Pipeline (`app.pipeline`)**: Orchestrator layer. May import from `app.retrieval`, `app.generation`, and `app.config`. Never imports `app.api`.
   - **API Routes (`app.api.routes`)**: Interface layer. May import from `app.pipeline`, `app.generation.llm`, and `app.config`.
2. **Absolute Module Paths**:
   - Always use absolute imports rooted at `app`: e.g., `from app.pipeline import pipeline`, not relative imports across packages.

---

## Where New Code Goes

- **New REST API Endpoints or Middleware**: Add to `app/api/routes.py`.
- **New Retrieval Strategy or Vector Search Enhancements**: Add to `app/retrieval/retriever.py`.
- **Alternative Reranking Models or Scoring Logic**: Add to `app/retrieval/reranker.py`.
- **Prompt Adjustments, Few-Shot Examples, Guardrails**: Add to `app/generation/prompt.py`.
- **LLM Provider Integrations or Retry Handlers**: Add to `app/generation/llm.py`.
- **Data Loaders, Cleaning Regex, Chunking Logic**: Add to `app/ingestion/loaders.py`, `app/ingestion/cleaner.py`, or `app/ingestion/chunker.py`.
- **Standalone Batch Jobs or Maintenance Tasks**: Add to `scripts/`.
- **Benchmarks, Latency Profilers, Unit Tests**: Add to `tests/`.
