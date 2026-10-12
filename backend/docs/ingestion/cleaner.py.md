# `cleaner.py` Documentation

### 1. Purpose
Normalizes text, strips OCR/PDF conversion artifacts, removes page markers, and collapses excessive whitespace.

### 2. What It Does
- `clean_text(text: str)`: Removes form-feed characters, strips `[PAGE N]` and standalone page numbers, normalizes Windows line endings, cleans trailing spaces, and standardizes markdown header spacing.

### 3. Depends on / Used by
- **Depends on**: Python standard library `re`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To strip new artifact patterns (e.g. copyright notices or headers), add a regex pattern using `re.sub(pattern, replacement, text)`.
2. Ensure new regex patterns do not inadvertently strip meaningful exercise tables or markdown syntax.
3. Test by running `clean_text` on sample text strings.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: Regex normalization, string sanitizers, character encoding cleansers, and whitespace formatters.
- **Do NOT add here**: File loading logic or vector database operations.
