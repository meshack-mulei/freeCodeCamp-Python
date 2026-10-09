### Build a Travel Weather Planner

Demonstrates rule-based decision trees for transport mode selection based on distance thresholds, weather conditions, and available transit assets:

- **Distance-Based Routing Tiers**: Categorizes travel routes into distinct distance brackets (immediate, short-distance, mid-range, long-distance).
- **Environmental & Asset Guardrails**: Evaluates weather impediments alongside personal transport availability (bicycles, vehicles, ride-share applications) to return accurate commute feasibility states.

```python
# Multi-modal commute feasibility logic
if distance_mi <= 1:
    print(not is_raining)  # Walk feasibility
elif distance_mi <= 6:
    print(has_bike and not is_raining)  # Bike feasibility
else:
    print(has_car or has_ride_share_app)  # Vehicular feasibility