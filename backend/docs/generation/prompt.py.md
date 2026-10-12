# `prompt.py` Documentation

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
