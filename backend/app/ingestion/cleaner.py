"""Cleans formatting artifacts and normalizes text from converted markdown documents."""
import re

def clean_text(text: str) -> str:
    """Cleans formatting artifacts and normalizes whitespace in raw markdown text.

    Steps:
        1. Remove form-feed and page-break characters.
        2. Remove explicit page markers such as [PAGE 23].
        3. Remove standalone lines containing only page numbers.
        4. Normalize Windows carriage return line endings to standard newlines.
        5. Strip trailing whitespace from the end of each line.
        6. Collapse three or more consecutive newlines down to double newlines.
        7. Collapse repeated inline whitespace down to single spaces.
        8. Standardize spacing immediately following Markdown heading markers.
        9. Strip leading and trailing whitespace from the resulting text.

    Args:
        text: Raw text string loaded from a document.

    Returns:
        Cleaned, normalized text string suitable for chunking.

    Raises:
        None.
    """
    # Remove form-feed/page-break characters
    text = text.replace("\f", "")

    # Remove explicit page markers like [PAGE 23]
    text = re.sub(r"\[PAGE\s+\d+\]", "", text, flags=re.IGNORECASE)

    # Remove lines containing only a page number
    text = re.sub(r"(?m)^\s*\d+\s*$", "", text)

    # Normalize Windows line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing whitespace from each line
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)

    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Collapse excessive spaces (but preserve newlines)
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Remove spaces directly inside Markdown heading markers
    text = re.sub(r"^(#{1,6})\s+", r"\1 ", text, flags=re.MULTILINE)

    return text.strip()







