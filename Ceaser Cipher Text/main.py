from alphabet import alphabet

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_str = ''
    for letter in text:
        position = alphabet.index(letter)
        if position + shift > 25:
            position =  (position + shift) - 26
            encrypted_str += alphabet[position]
        else:
            encrypted_str += alphabet[position + shift]
    print(f'Encrypted string is: {encrypted_str}')

encrypt(text=text, shift=shift)