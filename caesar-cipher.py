alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def translate(direction_toggle, plain_text, shift_amount):
    new_text = ""
    if direction_toggle == "encode":
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
            new_text += new_letter
    elif direction_toggle == "decode":
        for letter in plain_text:
            # Get the index number of that letter in the alphabet
            position = alphabet.index(letter)
            # Get the new position
            new_position = position-shift_amount
            # Get the new letter based on the new position. Error handle for positions higher than alphabet length
            if new_position >= 0:
                new_letter = alphabet[new_position]
            else:
                new_letter = alphabet[new_position+len(alphabet)]
            # Added new letter to encrypted text
            new_text += new_letter
    else:
        print("Please use encode or decode only!")
    print(f"The {direction_toggle}d text is {new_text}")


translate(direction,text,shift)