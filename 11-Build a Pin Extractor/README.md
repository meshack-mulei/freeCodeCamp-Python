### Build a Pin Extractor

Demonstrates nested text decomposition, positional word analysis, and boundary fallback handling for multi-line string datasets:

- **Hierarchical Text Processing**: Parses collection lists by iterating through multi-line poem strings, splitting lines by newline delimiters (`\n`), and tokenizing words via whitespace splitting.
- **Positional Extraction Algorithm**: Matches the zero-indexed line position ($N$) to the $N$-th word in that line, encoding character lengths into a sequential PIN string.
- **Index Guardrail Handling**: Incorporates explicit length checks (`len(words) > line_index`) to gracefully append a default `'0'` whenever a line lacks sufficient tokens, avoiding `IndexError` runtime exceptions.

```python
# Positional token extraction with length guardrails
for line_index, line in enumerate(lines):
    words = line.split()
    if len(words) > line_index:
        secret_code += str(len(words[line_index]))
    else:
        secret_code += '0'  # Fallback for short lines