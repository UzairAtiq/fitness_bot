"""Coordinates end-to-end RAG pipeline across retrieval, reranking, and generation."""
from app.retrieval.retriever import retrieve
from app.retrieval.reranker import reranker
from app.generation.prompt import build_prompt
from app.generation.llm import send_prompt

def pipeline(query: str, debug: bool = False):
    """Executes the end-to-end question answering pipeline for a user query.

    Steps:
        1. Retrieve candidate document chunks from Qdrant Cloud vector search.
        2. Rerank candidate chunks using the cross-encoder to select top relevant context.
        3. Build structured prompt with domain guardrails and selected context.
        4. Invoke Groq LLM to generate grounded response.
        5. If debug is True, compile chunk metadata and return (answer, chunk_info) tuple; otherwise return answer.

    Args:
        query: User query question string.
        debug: Whether to return retrieved chunk diagnostic metadata alongside the answer (default: False).

    Returns:
        Generated answer string, or tuple of (answer, chunk_info) if debug is True.

    Raises:
        Exception: If retrieval, reranking, or LLM generation encounters an unhandled failure.
    """
    # Sending query to retriever
    chunks_recieved = retrieve(query) 

    # Sending the query and top-k chunks to reranker for better ranking
    reranked_chunks = reranker(query, chunks_recieved)

    # Building the prompt
    prompt = build_prompt(query, reranked_chunks)

    # Sending the prompt to the llm and getting answer
    answer = send_prompt(prompt)

    # Getting the chunk headers and text to return when debugging
    if debug is True:
        chunk_info = [
            {
                "header": chunk.payload.get("header", "N/A"),
                "score": chunk.score,
                "Book": chunk.payload.get("doc_id"),
            }
            for chunk in reranked_chunks
        ]
        return answer, chunk_info

    return answer



