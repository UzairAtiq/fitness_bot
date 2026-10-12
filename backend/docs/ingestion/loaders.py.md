# `loaders.py` Documentation

### 1. Purpose
Reads raw text files from the local filesystem with UTF-8 encoding.

### 2. What It Does
- `load_book(path: str)`: Opens a file path in UTF-8 read mode and returns the complete text content as a string.

### 3. Depends on / Used by
- **Depends on**: Python standard library `open`.
- **Used by**: `scripts/ingest.py`.

### 4. How to Modify
1. To support additional file encodings or error handlers, pass parameters into `open()` inside `load_book`.
2. To support directory traversal or multiple file loading, add a `load_directory(dir_path)` function.
3. Test loading by executing `python -c "from app.ingestion.loaders import load_book; print(len(load_book('backend/data/raw/joe-weider-s-bodybuilding-system-joe-weider-2929.md')))"`.

### 5. What to Add Here / What NOT to Add Here
- **Add here**: File I/O readers for raw documents (text, markdown, PDF).
- **Do NOT add here**: Text cleaning logic (which belongs in `cleaner.py`) or chunk splitting logic.
