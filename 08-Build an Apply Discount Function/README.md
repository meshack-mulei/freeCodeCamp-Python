### Build an Apply Discount Function

Demonstrates guard clause patterns and rigorous input boundary validation for transactional price calculations:

- **Early Return Guard Clauses**: Validates inputs sequentially at the function entry point, returning descriptive error messages without unnecessary code nesting.
- **Strict Type Checking**: Restricts function inputs to valid numerical primitives (`int`, `float`) to guard against runtime type coercion errors.
- **Domain Constraint Enforcement**: Ensures business rule compliance by verifying that price figures remain strictly positive and discount rates fall within a standard percentage range ($0\text{--}100\%$).

```python
# Guard clause pattern for defensive price calculation
def apply_discount(price, discount):
    if type(price) not in [int, float]:
        return 'The price should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
        
    return price - (price * (discount / 100))