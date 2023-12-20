alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
word_len = len(text)

# Encrypt function
def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for letter in plain_text:
        # Get the index number of that letter in the alphabet
        position = alphabet.index(letter)
        # Get the new position
        new_position = position+shift_amount
        # Get the new letter based on the new position. Error handle for positions higher than alphabet length
        if new_position < len(alphabet):
            new_letter = alphabet[new_position]
        else:
            new_letter = alphabet[new_position-len(alphabet)]
        # Added new letter to encrypted text
        encrypted_text += new_letter
    print(f"The encoded text is {encrypted_text}")

encrypt(text,shift)