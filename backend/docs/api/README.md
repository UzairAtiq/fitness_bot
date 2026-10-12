# API Documentation & Reference

### Purpose
Exposes HTTP REST API endpoints using FastAPI, handles CORS middleware, validates timing-safe authentication access keys, and delegates queries to the RAG pipeline.

### File List
- **[routes.py](routes.py.md)**: Defines endpoints (`/health`, `/verify-key`, `/ask`), middleware, and access control.

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
