LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def translate_message(message, key, mode):
    translated = []
    key_index = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            if mode == 'encrypt':
                num += LETTERS.find(key[key_index])
            elif mode == 'decrypt':
                num -= LETTERS.find(key[key_index])
            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1

            if key_index >= len(key):
                key_index = 0

        else:
            translated.append(symbol)

    return ''.join(translated)


def encrypt(message, key):
    return translate_message(message, key, 'encrypt')


def decrypt(message, key):
    return translate_message(message, key, 'decrypt')


if __name__ == '__main__':
    plaintext = 'Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist.'
    key = 'ASIMOV'
    encrypted = encrypt(plaintext, key)
    decrypted = decrypt(encrypted, key)
    print(encrypted)
    print(decrypted)
