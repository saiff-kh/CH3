from random import randint

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text,key):

    text = text.upper()
    cipher_text=''

    for index,char in enumerate(text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text +=ALPHABET[(char_index + key_index)%len(ALPHABET)]
    
    return cipher_text



def decrypt(cipher_text,key):

    plain = ''

    for index , char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)

        plain+=ALPHABET[(char_index - key_index) % len(ALPHABET)]
    
    return plain


def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0,len(ALPHABET)-1))

    return random

masseg = 'Crypto is short for cryptocurrency which is a digital or virtual currency that uses cryptography '
seq = random_sequence(masseg)
print("Original message : %s" % masseg.upper())
cipher = encrypt(masseg,seq)
print("encrypted message: %s" % cipher)
decrypt_text = decrypt(cipher,seq)
print("Decrypted message : %s" % decrypt_text)
