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

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has 
#guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
while display.count("_") > 0:
    guess = input("Guess a letter. ").lower()

    #Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

print("You've won!")