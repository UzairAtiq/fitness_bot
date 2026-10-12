"""Loads raw text from markdown files on the local filesystem."""

def load_book(path: str) -> str:
    """Reads and loads text content from a specified markdown book file.

    Steps:
        1. Open the file at the specified path in read mode with UTF-8 encoding.
        2. Read the entire text contents into memory.
        3. Return the loaded text content.

    Args:
        path: Filesystem path to the source file to load.

    Returns:
        The complete text content of the file as a string.

    Raises:
        FileNotFoundError: If the file does not exist at the given path.
        OSError: If reading the file fails due to system or permission errors.
    """
    with open(path, "r", encoding="utf-8") as file: 
        text_content = file.read()
        return text_content
