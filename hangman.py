import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

#Testing code
print(f"pssst, the solution is {chosen_word}")

#Create blanks
display = []
for char in chosen_word:
    display += "_"

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter. ").lower()

    #Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You've won!")
