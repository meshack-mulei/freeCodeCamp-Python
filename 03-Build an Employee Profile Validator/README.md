### Employee Profile Validator

Demonstrates string operations for cleaning, parsing, and validating user data (e.g., emails, phone numbers, names, addresses):

- **Data Normalization**: Method chaining (`.strip().title()`, `.strip().lower()`) to sanitize whitespace and standardize case formats across inputs.
- **Dynamic Parsing & Reformatting**: Splits comma-delimited strings (`.split()`), replaces characters (`.replace()`), and constructs clean display identifiers from email usernames.
- **Validation & Pattern Matching**: Uses `.find()`, membership checks (`in`), prefix/suffix inspection (`.startswith()`, `.endswith()`), and character counts (`.count()`).

```python
# Email normalization & username extraction
messy_email = '   SARAH.DAVIS@COMPANY.COM   '
clean_email = messy_email.strip().lower()  # 'sarah.davis@company.com'

# Extract username dynamically based on delimiter position
at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]         # 'sarah.davis'
display_name = email_user.replace('.', ' ').title() # 'Sarah Davis'