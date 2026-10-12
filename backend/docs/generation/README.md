# Generation Package Documentation

### Purpose
Manages domain prompt engineering, guardrails enforcement, ChatGroq LLM client instantiation, and rate-limit handling.

### File List
- **[prompt.py](prompt.py.md)**: System prompt template, domain restriction rules, and prompt formatting.
- **[llm.py](llm.py.md)**: ChatGroq initialization, invocation, and rate-limit error detection.

### Import Rules
- **Can Import**: `app.config`.
- **Cannot Be Imported By**: `app.ingestion` or `app.retrieval`.
- **Imported By**: `app.pipeline` and `app.api.routes`.

### Where New Code Goes
- **Prompt Guardrails & Styling Instructions**: Add to `app/generation/prompt.py`.
- **Alternative LLM Providers or Fallback Models**: Add to `app/generation/llm.py`.
- **Output Parsers**: Add new parser modules inside `app/generation/`.
