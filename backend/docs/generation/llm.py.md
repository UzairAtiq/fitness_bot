# `llm.py` Documentation

### 1. Purpose
Initializes the Groq LLM client and provides resilient prompt invocation with token-per-minute and rate-limit error handlers.

### 2. What It Does
- `is_token_limit_error(err: Exception)`: Inspects HTTP status codes (413, 429) and error strings to detect rate limits.
- `send_prompt(prompt: str)`: Sends the assembled prompt to ChatGroq, catches rate limits to return a friendly user message, and returns the response string.

### 3. Depends on / Used by
- **Depends on**: `langchain_groq.ChatGroq`, `app.config.GROQ_API_KEY`.
- **Used by**: `app.pipeline.pipeline` and `app.api.routes.ask`.

### 4. How to Modify
1. To change the target Groq model (e.g., to `llama-3.3-70b-versatile`), update the `model` argument in the `ChatGroq` constructor.
2. To modify temperature or inference penalties, adjust constructor parameters in `llm.py`.
3. Test inference behavior by running `python backend/tests/benchmark_pipeline.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: LLM model configuration, client retry decorators, and model-specific exception mappings.
- **Do NOT add here**: System prompt strings (which belong in `prompt.py`) or database vector queries.
