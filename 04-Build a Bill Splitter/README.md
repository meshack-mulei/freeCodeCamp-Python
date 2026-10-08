### A Bill Splitter

Demonstrates arithmetic computation, running total aggregation, and financial precision handling for group bill calculations:

- **State Management**: Uses compound assignment operators (`+=`) to dynamically track cumulative costs and tip percentages.
- **Fair Allocation Logic**: Evaluates individual cost distribution by dividing total aggregated costs across group members.
- **Precision Formatting**: Converts floating-point arithmetic outputs into standardized currency amounts using `round()`.

```python
# Calculating per-person split with tip
running_total = 0
running_total += appetizers + main_courses + desserts + drinks

# Compound tip calculation & per-person distribution
running_total += running_total * 0.25
each_pays = round(running_total / num_of_friends, 2)