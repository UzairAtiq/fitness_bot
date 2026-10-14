"""FastAPI route handlers and middleware for question answering and authentication."""
import secrets
from fastapi import FastAPI, Header, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.config import SHARED_ACCESS_KEY
from app.pipeline import pipeline
from app.generation.llm import is_token_limit_error, TOKEN_LIMIT_MESSAGE

# initialize fastapi app
app = FastAPI(title="Fitness Bot API")

# configure cors to allow requests from cloudfront and local dev servers
origins = [
    "https://d1kipqqm1ofiqs.cloudfront.net",
    "https://fitnessbot.uzairatiq.app",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    """Request payload schema for query execution.

    Attributes:
        query: User input text question string.
    """
    query: str


def check_access_authorization(x_access_key: str | None) -> None:
    """Verifies client access key against the configured server secret.

    Steps:
        1. Check if SHARED_ACCESS_KEY is set on the server.
        2. Normalize whitespace and surrounding quotes on server and client keys.
        3. Verify key presence and compare using constant-time secrets.compare_digest.
        4. Raise HTTP 401 Unauthorized exception if keys do not match.

    Args:
        x_access_key: Client-provided access key string from the request header.

    Returns:
        None.

    Raises:
        HTTPException: If access key is missing or fails constant-time comparison (401 Unauthorized).
    """
    # if shared access key is configured on server, require exact match (normalizing quotes)
    if SHARED_ACCESS_KEY:
        server_key = SHARED_ACCESS_KEY.strip().strip('"').strip("'")
        client_key = (x_access_key or "").strip().strip('"').strip("'")
        if not client_key or not secrets.compare_digest(client_key, server_key):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing access key. Please enter the correct password.",
            )


# health check endpoint to verify backend status (unauthenticated for monitoring)
@app.get("/health")
def health():
    """Returns service health status for uptime monitoring.

    Steps:
        1. Assemble status response dictionary.
        2. Return status dictionary.

    Args:
        None.

    Returns:
        Dictionary confirming service availability status.

    Raises:
        None.
    """
    return {"status": "ok", "service": "Fitness Bot API"}


# quick verification endpoint for frontend access code modal
@app.post("/verify-key")
def verify_key(x_access_key: str | None = Header(None, alias="x-access-key")):
    """Validates provided access key from frontend authorization modal.

    Steps:
        1. Invoke check_access_authorization with header key.
        2. Return valid flag if check succeeds.

    Args:
        x_access_key: Access key string provided via x-access-key HTTP header.

    Returns:
        Dictionary indicating validation status.

    Raises:
        HTTPException: 401 Unauthorized if access key is invalid.
    """
    check_access_authorization(x_access_key)
    return {"valid": True}


# handle ask query request from frontend
@app.post("/ask")
def ask(
    request: QueryRequest,
    x_access_key: str | None = Header(None, alias="x-access-key"),
):
    """Authenticates request and executes question query through RAG pipeline.

    Steps:
        1. Authenticate request using check_access_authorization.
        2. Strip whitespace from input query and validate non-empty string.
        3. Invoke pipeline to retrieve chunks, rerank, and generate response.
        4. Catch and handle Qdrant connection resets and Groq rate limit errors.
        5. Return dictionary containing answer text.

    Args:
        request: QueryRequest payload containing the query string.
        x_access_key: Access key string provided via x-access-key HTTP header.

    Returns:
        Dictionary containing the generated answer string.

    Raises:
        HTTPException: 401 Unauthorized if access key authentication fails.
    """
    # authenticate request against shared secret
    check_access_authorization(x_access_key)

    cleaned_query = request.query.strip()
    if not cleaned_query:
        return {"answer": "Please provide a training, workout, or nutrition question."}

    try:
        answer = pipeline(cleaned_query)
        return {"answer": answer}
    except Exception as pipeline_err:
        err_msg = str(pipeline_err)
        print(f"pipeline query failed: {err_msg}")

        # handle qdrant cloud connection resets
        if "Connection reset by peer" in err_msg or "ResponseHandlingException" in err_msg:
            return {
                "answer": (
                    "⚠️ **Could not connect to Qdrant Cloud**:\n\n"
                    "The remote Qdrant Cloud cluster reset the connection (`[Errno 54] Connection reset by peer`).\n\n"
                    "Please check your cluster status at [cloud.qdrant.io](https://cloud.qdrant.io) to ensure the cluster is active (not paused or hibernated)."
                )
            }

        # handle groq token limit and rate limit errors
        if is_token_limit_error(pipeline_err):
            return {"answer": TOKEN_LIMIT_MESSAGE}

        return {"answer": f"⚠️ An error occurred during retrieval or generation:\n\n{err_msg}"}
