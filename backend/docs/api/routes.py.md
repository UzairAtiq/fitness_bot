# `routes.py` Documentation

### 1. Purpose
Defines FastAPI application instance, CORS configuration, authentication helper, and REST endpoints for health checks, access validation, and query answering.

### 2. What It Does
- `QueryRequest`: Pydantic model validating incoming JSON request payloads containing the `query` string.
- `check_access_authorization(x_access_key: str | None)`: Validates header access keys using timing-safe comparison against `SHARED_ACCESS_KEY`.
- `health()`: Unauthenticated health check endpoint returning HTTP 200 with service status.
- `verify_key(x_access_key)`: Validates guest or admin access codes for the frontend lock modal.
- `ask(request, x_access_key)`: Authenticates user, forwards questions to `pipeline()`, handles Qdrant/Groq errors, and returns answers.

### 3. Depends on / Used by
- **Depends on**: `fastapi`, `app.config.SHARED_ACCESS_KEY`, `app.pipeline.pipeline`, `app.generation.llm.is_token_limit_error`.
- **Used by**: Uvicorn web server and frontend API clients calling HTTP endpoints.

### 4. How to Modify
1. To add a new endpoint, decorate a new handler function with `@app.get` or `@app.post`.
2. To require authentication on the new endpoint, invoke `check_access_authorization(x_access_key)` inside the handler.
3. Restart or reload Uvicorn (`uvicorn app.api.routes:app --reload`) and test using `curl`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: HTTP routing logic, request parsing models, status codes, and HTTP-specific error translation.
- **Do NOT add here**: Low-level database operations, direct LLM prompt formatting, or document chunking algorithms.
