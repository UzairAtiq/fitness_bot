# `chunker.py` Documentation

### 1. Purpose
Splits cleaned markdown text into document chunks while preserving heading hierarchy (H1 through H4) in metadata.

### 2. What It Does
- `chunk_document(cleaned_text: str)`: Configures `MarkdownHeaderTextSplitter` with `#`, `##`, `###`, and `####` headers, and splits text into structured LangChain `Document` chunks.

### 3. Depends on / Used by
- **Depends on**: `langchain_text_splitters.MarkdownHeaderTextSplitter`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To change the headers split on or add deeper levels (e.g., `#####`), edit `headers_to_split_on`.
2. To apply a character-level secondary split for extra-long sections, chain `RecursiveCharacterTextSplitter` after the markdown header split.
3. Test chunking by verifying chunk counts and metadata headers on sample texts.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Document chunking, text splitting, token count estimators, and chunk boundary algorithms.
- **Do NOT add here**: Text cleaning regex (which belongs in `cleaner.py`) or embedding computations.
