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

## Code Structure & Logic

### 1. `find_invalid_records`
Accepts field values as keyword arguments, evaluates each field against defined constraints, and returns a list of keys that failed validation:
- **Patient ID**: Must match regex `r'p\d+'` (e.g., `P1001`).
- **Age**: Must be an integer $\ge 18$.
- **Gender**: Case-insensitive match against `['male', 'female']`.
- **Medications**: Must be a list where every element is a string.
- **Last Visit ID**: Must match regex `r'v\d+'` (e.g., `V2301`).

### 2. `validate`
Iterates over a list of medical record dictionaries and evaluates structural and constraint validity:
1. Confirms the dataset is a list or tuple.
2. Checks that each element is a dictionary with exact expected keys.
3. Unpacks valid dictionaries into `find_invalid_records()`.
4. Prints formatted warning messages for invalid fields along with their index position in the dataset.
