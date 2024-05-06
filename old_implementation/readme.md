# Vignere Cipher 🔒

A simple and efficient Python implementation of the Vignere Cipher, a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword.

## Features 🚀

- Encryption of plaintext messages
- Decryption of ciphertext messages
- Comprehensive mapping of letters to their corresponding indexes
- Complete construction and manipulation of the Vignere Cipher table

## Code Structure 🗂

The code is divided into two main modules:

- `utils.py`: Contains various utility functions used throughout the project, such as generating a letter map, sanitizing input, and more.
- `vignere_cipher.py`: Contains the classes for mapping the letters to their corresponding indexes, constructing and manipulating Vignere Cipher table, and performing Vignere Cipher encryption and decryption.

## Usage 💡

Here's a simple example of how to use this library:

```python
from vignere_cipher import VignereCipher

plaintext = 'this is the message &^%^& it will be encrypted 012010220120121021102102101021'
key = 'SECRETKEY'

# Creating the Cipher instance
vc = VignereCipher()

# Encryption
ciphertext = vc.encrypt(plaintext, key)
print(ciphertext)

# Decryption
print(vc.decrypt(ciphertext, key))

```

## Enjoy coding! 🎉