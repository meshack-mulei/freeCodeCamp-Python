## Report Card Printer

Demonstrates type checking and variable initialization for individual student records prior to generating formatted report cards:

- **Student Attribute Management**: Captures key student properties including string identifiers (`name`), boolean enrollment status (`is_student`), integer age (`age`), and floating-point academic scores (`score`).
- **Defensive Type Checking**: Utilizes `isinstance()` to validate numeric types (`float`) before processing grade logic, preventing runtime errors during score aggregation.

```python
# Student record attribute definition & runtime validation
name = 'Alice'
is_student = True
age = 20
score = 80.5

# Ensure score is a valid float before generating report card metrics
if isinstance(score, float):
    print(f"Validated score for {name}: {score}")