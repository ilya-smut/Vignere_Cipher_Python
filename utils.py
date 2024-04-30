import re

def fill_row(shift):
    # List of capital letters
    capital_letters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z']
    # Shift letters based on shift value
    shifted_letters = capital_letters[shift:] + capital_letters[:shift]
    return list(shifted_letters)

def generate_table():
    # Initialize 26x26 table with 'A'
    table = [['A']*26]*26
    # Fill each row with shifted letters
    for i in range(0, 26):
        table[i] = fill_row(i)
    return table

def generate_letter_map():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_mapping = {letter: index for index, letter in enumerate(alphabet)}
    index_mapping = {index: letter for index, letter in enumerate(alphabet)}
    return alphabet_mapping, index_mapping

def fit_string(string1, string2):
    if len(string1) <= len(string2):
        return string2[:len(string1)]
    else:
        repetitions = len(string1) // len(string2)
        remainder = len(string1) % len(string2)
        fitted_string = string2 * repetitions + string2[:remainder]
        return fitted_string

def sanitize_input(input_string):
    # Convert all letters to uppercase
    input_string = input_string.upper()
    # Remove everything but capital English letters
    sanitized_string = re.sub(r'[^A-Z]', '', input_string)
    return sanitized_string