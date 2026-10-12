### Build a User Configuration Manager

Demonstrates dictionary manipulation, tuple unpacking, and state validation for user preference configuration:

- **Tuple-Based Parameter Ingestion**: Unpacks incoming configuration parameters cleanly into key-value pairs.
- **Input Normalization**: Standardizes casing using `.lower()` to prevent duplicate keys due to capitalization variance.
- **Defensive CRUD Architecture**: Validates key existence prior to updates or deletions to avoid runtime exceptions and maintain stable system state.
