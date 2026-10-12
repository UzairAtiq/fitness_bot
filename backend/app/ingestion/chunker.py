"""Splits markdown text into structured chunks preserving heading hierarchy."""
from langchain_text_splitters import MarkdownHeaderTextSplitter

def chunk_document(cleaned_text: str) -> list:
    """Splits cleaned markdown text into document chunks based on header hierarchy.

    Steps:
        1. Define markdown header markers to split on (H1 through H4).
        2. Instantiate LangChain MarkdownHeaderTextSplitter with the specified headers.
        3. Split the cleaned text into chunked Document instances with header metadata.
        4. Return the list of split Document instances.

    Args:
        cleaned_text: Normalized markdown text to chunk.

    Returns:
        List of LangChain Document objects containing chunked text and header metadata.

    Raises:
        None.
    """

    # Defining Headers to split the text on 
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
        ("####", "Header 4"),
    ]

    # Passing the splitting headers to langchain splitter
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

    # Splitting the text based on headers
    md_header_splits = markdown_splitter.split_text(cleaned_text)

    return md_header_splits
