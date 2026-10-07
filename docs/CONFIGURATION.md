# Configuration

The application uses environment variables for backend and frontend services.

## Backend Configuration (`.env`)

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

### Required Keys

| Variable | Description |
| :--- | :--- |
| `QDRANT_URL` | Endpoint URL of your Qdrant Cloud cluster |
| `QDRANT_API_KEY` | API key for Qdrant Cloud |
| `GROQ_API_KEY` | Groq Cloud API key for model generation |
| `SHARED_ACCESS_KEY` | Password required by the frontend lock screen and API |

> **Local Development Note**: For local development, set `SHARED_ACCESS_KEY` in `.env` to any password you want (for example, `SHARED_ACCESS_KEY=my-local-secret`). When you open the frontend, enter that same password into the access lock screen to unlock the application.

### Optional Keys

| Variable | Default | Description |
| :--- | :--- | :--- |
| `collection_name` | `bodybuilding_rag` | Target collection name in Qdrant Cloud |

---

## Frontend Configuration (`frontend/.env`)

Create a `.env` file inside the `frontend/` directory if connecting to a non-default backend:

```bash
cp frontend/.env.example frontend/.env
```

| Variable | Default | Description |
| :--- | :--- | :--- |
| `VITE_BACKEND_URL` | `http://localhost:8000` | URL of the backend FastAPI service |
