### Build an RPG Character

Demonstrates multi-stage input validation, point-allocation guardrails, and string repetition for visual stat display generation:

- **Strict Attribute Guardrails**: Enforces valid character naming conventions (non-empty, maximum 10 characters, space-free) alongside bounded stat constraints ($1\text{--}4$ points per attribute).
- **Point Pool Enforcement**: Verifies that total allocated stats sum exactly to a starting budget of 7 points before creating the character model.
- **Visual Progress Bar Rendering**: Utilizes Python's string multiplication operator (`*`) to generate visual stat indicators using Unicode symbols (`●` and `○`).

```python
# Visual stat indicator generation via string multiplication
str_dots = (full_dot * strength) + (empty_dot * (10 - strength))
int_dots = (full_dot * intelligence) + (empty_dot * (10 - intelligence))
cha_dots = (full_dot * charisma) + (empty_dot * (10 - charisma))

# Multi-line formatted card output
return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"