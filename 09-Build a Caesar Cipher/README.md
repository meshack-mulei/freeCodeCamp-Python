### Build a Caesar Cipher

Demonstrates string translation algorithms, bidirectional transformation routines, and functional wrapper abstractions for classic text ciphers:

- **Dynamic Shift Mapping**: Generates custom character lookup maps using string slice concatenation (`alphabet[shift:] + alphabet[:shift]`).
- **High-Performance Substitution**: Utilizes Python's native `str.maketrans()` and `str.translate()` for efficient $O(1)$ character lookup operations across mixed-case text inputs.
- **Directional Flagging & Abstraction**: Employs boolean parameters (`encrypt=True/False`) to handle bidirectional offset math and exposes simple `encrypt()` and `decrypt()` API helpers.

```python
# Slicing-based character shift and translation table creation
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(
    alphabet + alphabet.upper(), 
    shifted_alphabet + shifted_alphabet.upper()
)

# Constant-time text transformation
encrypted_text = text.translate(translation_table)