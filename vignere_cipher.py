import utils

# Class for mapping the letters to their corresponding indexes
class LetterMap:
    def __init__(self):
        # Generate the map of letters to their indexes
        self.char_map, self.int_map = utils.generate_letter_map()

    # Method to match a character to its corresponding index
    def match_letter(self, char):
        if len(char) == 1:
            char = char.upper()
            return self.char_map[char]
        else:
            return None
        
    def match_index(self, int):
        if 0 <= int < 26:
            return self.int_map[int]

# Class to construct and manipulate Vignere cipher table
class VignereTable:
    def __init__(self):
        # Generate the Vignere cipher table
        self.table = utils.generate_table()
        self.letter_map = LetterMap()

    # Method to get the cipher character for a given letter and key
    def match_cipher(self, letter, key):
        letter_index = self.letter_map.match_letter(letter)
        key_index = self.letter_map.match_letter(key)
        return self.table[letter_index][key_index]

    # Method to find a plaintext character in a column given a key character and a cipher character
    def find_letter_in_a_column(self, column, letter):
        column = self.table[self.letter_map.match_letter(column)]
        for i in range(0, 26):
            if column[i] == letter:
                return self.letter_map.match_index(i)


# Class to perform Vignere cipher encryption and decryption
class VignereCipher:
    def __init__(self):
        self.vignere_table = VignereTable()

    # Method to encrypt a plaintext string given a key
    def encrypt(self, string, key):
        string = utils.sanitize_input(string)
        key = utils.sanitize_input(key)
        extended_key = utils.fit_string(string, key)
        ciphertext = ''
        for i in range(0, len(string)):
            ciphertext += self.vignere_table.match_cipher(string[i], extended_key[i])
        return ciphertext

    # Method to decrypt a ciphertext string given a key
    def decrypt(self, ciphertext, key):
        string = utils.sanitize_input(ciphertext)
        key = utils.sanitize_input(key)
        extended_key = utils.fit_string(ciphertext, key)
        plaintext = ''
        for i in range(0, len(ciphertext)):
            plaintext += self.vignere_table.find_letter_in_a_column(extended_key[i], ciphertext[i])
        return plaintext