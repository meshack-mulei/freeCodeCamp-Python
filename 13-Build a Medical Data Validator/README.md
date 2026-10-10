# Medical Record Data Validator

A Python project that validates complex structured medical dataset entries against schema constraints, field type rules, and format patterns.

## Features

- **Schema Integrity**: Verifies input types (lists/tuples of dictionaries) and checks for missing or extra keys.
- **Field-Level Validation**: Uses regular expressions and type checking to validate patient IDs, age, gender, diagnosis, medications, and visit IDs.
- **Detailed Error Logging**: Tracks invalid fields and logs precise error messages indicating the position of the record and the faulty key-value pair.

## Technical Highlights

- **Functional Architecture**: Separates constraint-checking logic (`find_invalid_records`) from dataset-level iteration and reporting (`validate`).
- **Python Conventions**:
  - `enumerate()` for zero-indexed positional error reporting.
  - Dictionary unpacking (`**dictionary`) for dynamic parameter passing.
  - List comprehensions with `all()` for iterating over iterable field checks (e.g., verifying lists of medication strings).
  - Regular expressions (`re.fullmatch` with `re.IGNORECASE`) for strict string format patterns.
