from vignere_cipher import VignereCipher

plaintext = 'this is the message &^%^& it will be encrypted 012010220120121021102102101021'
key = 'SECRETKEY'

vc = VignereCipher()

ciphertext = vc.encrypt(plaintext, key)
print(ciphertext)

print(vc.decrypt(ciphertext, key))