"""Initializes Groq LLM client and handles prompt invocation with error guards."""
from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY

# initialize groq llm
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    api_key=GROQ_API_KEY,
)

TOKEN_LIMIT_MESSAGE = (
    "⚠️ **Token limit exceeded**: The request exceeded the model's token limit (tokens per minute). "
    "Please wait a moment and try again."
)

def is_token_limit_error(err: Exception) -> bool:
    """Checks whether an exception corresponds to a Groq token limit or rate limit error.

    Steps:
        1. Inspect the status_code attribute on the exception if present.
        2. Return True if status code matches 413 or 429.
        3. Inspect the error message string for rate limit or token limit keywords.
        4. Return True if matching substrings are found, False otherwise.

    Args:
        err: Exception raised during LLM invocation.

    Returns:
        True if the exception represents a token or rate limit failure, False otherwise.

    Raises:
        None.
    """
    # check for groq 413 (request too large / tpm exceeded) or 429 (rate limit)
    status_code = getattr(err, "status_code", None)
    if status_code in (413, 429):
        return True

    err_str = str(err)
    return "rate_limit_exceeded" in err_str or "Request too large" in err_str

def send_prompt(prompt: str) -> str:
    """Sends a formatted prompt to the Groq LLM and retrieves the response.

    Steps:
        1. Invoke the ChatGroq model with the prompt string.
        2. Convert the response content to string and return.
        3. Catch exceptions during LLM invocation.
        4. Return a predefined message if the exception is a token or rate limit error.
        5. Re-raise any unhandled exceptions.

    Args:
        prompt: Formatted prompt text to send to the language model.

    Returns:
        Generated text response from the model or token limit warning message.

    Raises:
        Exception: If an unhandled API or network error occurs during invocation.
    """
    print("Sending prompt to LLM")

    try:
        response = llm.invoke(prompt)
        return str(response.content)
    except Exception as llm_err:
        print(f"LLM invocation error: {llm_err}")

        # handle groq token limit and rate limit errors directly
        if is_token_limit_error(llm_err):
            return TOKEN_LIMIT_MESSAGE

        raise