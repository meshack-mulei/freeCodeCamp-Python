### Employee Profile Generator

Demonstrates string operations, f-string formatting, and slice-based parsing for employee records:

- **Data Concatenation & Formatting**: Constructs composite strings and formats structured records using both traditional concatenation and modern f-strings.
- **Identifier Parsing**: Uses Python string slicing (`[start:end]`, negative indices) to extract embedded metadata (department, year, initials, sequence) from formatted employee codes.

```python
# Parsing structured employee code
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]  # 'DEV'
year_code = employee_code[4:8]    # '2026'
initials = employee_code    # 'JD'
last_three = employee_code[-3:]   # '001'