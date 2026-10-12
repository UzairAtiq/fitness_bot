# Project Structure

Overview of the repository organization and file structure.

```text
Muscle_Info_RAG/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py             # FastAPI endpoints (/ask, /verify-key, /health) and CORS
│   │   ├── generation/
│   │   │   ├── llm.py                # Groq ChatGroq client and rate-limit handlers
│   │   │   └── prompt.py             # Prompt template with bodybuilding domain guardrails
│   │   ├── ingestion/
│   │   │   ├── cleaner.py            # Text normalization and whitespace cleaning
│   │   │   ├── chunker.py            # MarkdownHeaderTextSplitter (Headers 1-4)
│   │   │   ├── indexer.py            # Qdrant collection setup, embedding, and upserting
│   │   │   └── loaders.py            # Markdown file loader
│   │   ├── retrieval/
│   │   │   ├── reranker.py           # Cross-encoder reranking model and scoring
│   │   │   └── retriever.py          # Qdrant client retrieval function
│   │   ├── config.py                 # Loads environment variables
│   │   └── pipeline.py               # End-to-end RAG pipeline
│   ├── data/
│   │   ├── evaluation/
│   │   │   └── evaluate.json         # Output results from evaluation runs
│   │   └── raw/
│   │       └── joe-weider-...md      # Source course text in Markdown
│   ├── scripts/
│   │   ├── evaluate.py               # 8-question evaluation script
│   │   └── ingest.py                 # Chunks, embeds, and indexes source documents
│   ├── tests/
│   │   ├── benchmark_pipeline.py     # Latency and memory profiling script
│   │   ├── test_ingestion.py         # Test stub for ingestion
│   │   ├── test_pipeline.py          # Test stub for pipeline
│   │   └── test_retrieval.py         # Test stub for retrieval
│   ├── .env.example                  # Backend environment variables template
│   └── requirements.txt              # Pinned Python dependencies
├── assets/
│   └── github.gif                    # Project demo animation
├── docker/
│   ├── Dockerfile                    # Container configuration with pre-cached models
│   └── docker-compose.yml            # Local container orchestration
├── docs/
│   ├── ARCHITECTURE.md               # System architecture and RAG pipeline flow
│   ├── CONFIGURATION.md              # Environment variables and configuration
│   ├── DEPLOYMENT.md                 # AWS production and local Docker deployment
│   ├── PROJECT_STRUCTURE.md          # Repository layout and file descriptions
│   └── TESTING.md                    # Benchmarks and evaluation scripts
├── frontend/
│   ├── src/
│   │   ├── components/               # AccessModal, Header, Sidebar, Chatbox, ChatInput, ChatMessage
│   │   ├── hooks/                    # Typewriter animation hook
│   │   ├── services/                 # API client connecting to FastAPI (/ask, /verify-key)
│   │   ├── types/                    # Session, message, and query status types
│   │   ├── App.tsx                   # Main application state and session management
│   │   └── main.tsx                  # React entry point
│   ├── index.html                    # HTML template with cache prevention meta tags
│   ├── package.json                  # Frontend dependencies and npm scripts
│   └── vite.config.ts                # Vite build configuration and path aliases
├── .dockerignore                     # Build context exclusions
└── README.md
```
