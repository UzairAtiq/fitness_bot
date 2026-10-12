"""Loads environment variables and defines global configuration settings."""
import os 
from pathlib import Path
from dotenv import load_dotenv

backend_env = Path(__file__).resolve().parent.parent / ".env"
root_env = Path(__file__).resolve().parent.parent.parent / ".env"
if backend_env.exists():
    load_dotenv(backend_env)
elif root_env.exists():
    load_dotenv(root_env)
else:
    load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
collection_name = os.getenv("collection_name", "bodybuilding_rag")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROK_API_KEY = GROQ_API_KEY
SHARED_ACCESS_KEY = os.getenv("SHARED_ACCESS_KEY")

