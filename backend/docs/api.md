# API Documentation

### Purpose
Exposes HTTP REST API endpoints using FastAPI, handles CORS middleware, validates timing-safe authentication access keys, and delegates queries to the RAG pipeline.

### Import Rules
- **Can Import**: `app.config`, `app.pipeline`, and `app.generation.llm`.
- **Cannot Be Imported By**: Lower layers (`app.ingestion`, `app.retrieval`, `app.generation`, or `app.pipeline`). The API package is an edge interface layer.

### Where New Code Goes
- **New REST Endpoints**: Add route decorators (`@app.get`, `@app.post`) and handler functions inside `app/api/routes.py`.
- **New Request/Response Models**: Define Pydantic models inheriting from `BaseModel` in `app/api/routes.py`.
- **New Middleware**: Attach middleware using `app.add_middleware(...)` in `app/api/routes.py`.

---

## Endpoints

| Method | Endpoint | Auth Required | Request Details | Response |
| :--- | :--- | :---: | :--- | :--- |
| `GET` | `/health` | No | None | `{"status": "ok", "service": "Fitness Bot API"}` |
| `POST` | `/verify-key` | Yes | Header: `x-access-key: <key>` | `{"valid": true}` (or 401 Unauthorized) |
| `POST` | `/ask` | Yes | Header: `x-access-key: <key>`<br>JSON: `{"query": "string"}` | `{"answer": "string"}` |

---

## Example Request

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -H "x-access-key: your-secret-password" \
  -d '{"query": "What exercises primarily target the triceps?"}'
```

---

## Example Response

```json
{
  "answer": "### Triceps Targeted Exercises\n\n- **Close-Grip Bench Press**: Places primary mechanical tension on the inner triceps heads while minimizing shoulder involvement.\n- **Triceps Extension (Lying/Standing)**: Isolates the long head of the triceps through full elbow extension."
}
```

---

## Module Reference: `routes.py`

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
