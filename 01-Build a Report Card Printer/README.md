## Report Card Printer

Demonstrates fundamental Python data types and runtime type inspection:

- **Data Types Covered**: Strings (`str`), Booleans (`bool`), Integers (`int`), and Floating-point numbers (`float`).
- **Type Inspection**: Uses `type()` to output runtime classes and `isinstance()` to evaluate data type conditions programmatically.

```python
# Type inspection example
score = 80.5
print(isinstance(score, float)) # Returns True
print(score, type(score))       # Outputs: 80.5 <class 'float'>