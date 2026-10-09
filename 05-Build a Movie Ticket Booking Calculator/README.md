### A Movie Ticket Booking Calculator

Demonstrates decision tree logic, multi-condition evaluation, and conditional fee processing for event ticketing workflows:

- **Access & Eligibility Controls**: Evaluates age and show-time restrictions using combined logical operators (`and`, `or`, `not`).
- **Dynamic Surcharge & Discount Engine**: Applies surcharges based on temporal triggers (weekend/evening rates) and calculates promotional discounts based on membership tier.
- **Multi-Tiered Service Fee Calculation**: Utilizes `if-elif-else` structures to assign tier-specific service charges (`Premium`, `Gold`, `standard`) before computing net order totals.

```python
# Multi-condition access evaluation & price compilation
if age >= 21 or (age >= 18 and (show_time != 'Evening' or is_member)):
    # Tier-based service charge calculation
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    # Dynamic final price accumulation
    final_price = base_price + extra_charges + service_charges - discount