# Generation Documentation

### Purpose
Manages domain prompt engineering, guardrails enforcement, ChatGroq LLM client instantiation, and rate-limit handling.

### Import Rules
- **Can Import**: `app.config`.
- **Cannot Be Imported By**: `app.ingestion` or `app.retrieval`.
- **Imported By**: `app.pipeline` and `app.api.routes`.

### Where New Code Goes
- **Prompt Guardrails & Styling Instructions**: Add to `app/generation/prompt.py`.
- **Alternative LLM Providers or Fallback Models**: Add to `app/generation/llm.py`.
- **Output Parsers**: Add new parser modules inside `app/generation/`.

---

## Module Reference: `prompt.py`

### 1. Purpose
Defines system instructions, domain guardrails, and prompt formatting templates for bodybuilding consulting.

### 2. What It Does
- `BODYBUILDING_PROMPT_TEMPLATE`: Multi-line prompt template instructing the model to reject off-topic questions and format answers with clear markdown headers, bold terms, and bullet points.
- `build_prompt(query: str, ranked_chunks: list)`: Formats the template by joining retrieved chunk texts into a context block and binding the user question.

### 3. Depends on / Used by
- **Depends on**: `langchain_core.prompts.PromptTemplate`.
- **Used by**: `app.pipeline.pipeline` and `tests/benchmark_pipeline.py`.

### 4. How to Modify
1. To change the system instructions or add new guardrail clauses, edit `BODYBUILDING_PROMPT_TEMPLATE`.
2. To include additional metadata (such as chapter titles) in context blocks, modify `build_prompt` to extract those keys from `chunk.payload`.
3. Verify formatting output by running `python backend/tests/benchmark_pipeline.py --profile-only`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Prompt templates, few-shot examples, domain boundaries, and output formatting guidelines.
- **Do NOT add here**: LLM API keys or client network connection calls.

---

## Module Reference: `llm.py`

### 1. Purpose
Initializes the Groq LLM client and provides resilient prompt invocation with token-per-minute and rate-limit error handlers.

### 2. What It Does
- `is_token_limit_error(err: Exception)`: Inspects HTTP status codes (413, 429) and error strings to detect rate limits.
- `send_prompt(prompt: str)`: Sends the assembled prompt to ChatGroq, catches rate limits to return a friendly user message, and returns the response string.

### 3. Depends on / Used by
- **Depends on**: `langchain_groq.ChatGroq`, `app.config.GROQ_API_KEY`.
- **Used by**: `app.pipeline.pipeline` and `app.api.routes.ask`.

### 4. How to Modify
1. To change the target Groq model (e.g., to `llama-3.3-70b-versatile`), update the `model` argument in the `ChatGroq` constructor.
2. To modify temperature or inference penalties, adjust constructor parameters in `llm.py`.
3. Test inference behavior by running `python backend/tests/benchmark_pipeline.py`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: LLM model configuration, client retry decorators, and model-specific exception mappings.
- **Do NOT add here**: System prompt strings (which belong in `prompt.py`) or database vector queries.
