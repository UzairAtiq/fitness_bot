"""Ingests, cleans, chunks, and indexes source documents into Qdrant."""
from pathlib import Path
import sys

# ensure backend root is on sys.path
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.ingestion.chunker import chunk_document
from app.ingestion.loaders import load_book
from app.ingestion.indexer import indexer 
from app.ingestion.cleaner import clean_text
from app.config import collection_name

book_1 = "Joe_weider_Book"


def run_ingest() -> None:
    """Loads source book markdown, cleans formatting, chunks by headers, and indexes to Qdrant.

    Steps:
        1. Resolve source document markdown path relative to backend directory.
        2. Load book contents from disk using load_book.
        3. Clean formatting artifacts and page markers using clean_text.
        4. Split cleaned text into hierarchical chunks using chunk_document.
        5. Generate vector embeddings and upload points into Qdrant using indexer.

    Args:
        None.

    Returns:
        None.

    Raises:
        FileNotFoundError: If the source markdown file does not exist at the target path.
        Exception: If vector embedding or Qdrant upserting fails.
    """
    # Getting the file path relative to project root
    file_path = Path(__file__).resolve().parent.parent / "data" / "raw" / "joe-weider-s-bodybuilding-system-joe-weider-2929.md"

    # Load book as text
    loaded_book = load_book(file_path)

    # clean the text from loaded book 
    cleaned_text = clean_text(loaded_book)

    # split the cleaned text into chunks 
    chunked_document = chunk_document(cleaned_text)

    # embed the chunks and push to quadrant
    indexer(chunked_document, collection_name, book_1)


if __name__ == "__main__":
    run_ingest()
