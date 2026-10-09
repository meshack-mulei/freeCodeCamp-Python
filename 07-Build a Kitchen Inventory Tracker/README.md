### Build a Kitchen Inventory Tracker

Demonstrates function scoping, explicit state updates, and defensive resource tracking for kitchen inventory management:

- **Explicit State Mutation**: Avoids global scope pollution by returning updated variable states from functions and reassigning them at the caller level.
- **Defensive Inventory Controls**: Validates item thresholds before attempting resource consumption, returning original state balances if constraints fail.
- **Modular Function Composition**: Composes high-level recipe functions (`make_fried_egg`) using low-level inventory utility primitives (`use_eggs`).

```python
# Functional inventory update pattern
def make_fried_egg(available_eggs):
    if available_eggs >= 1:
        available_eggs = use_eggs(available_eggs, 1)
        print("Made a fried egg. Yummy!")
    return available_eggs

# Reassigning return value to update caller state safely
available_eggs = make_fried_egg(available_eggs)