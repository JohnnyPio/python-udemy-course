import random
import hangman_art
import hangman_words
import os

# Variables
chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
end_of_game = False
lives = 6

# clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Testing code
print(hangman_art.logo)
#print(f"pssst, the solution is {chosen_word}")

#Create blanks
display = []
for char in chosen_word:
    display += "_"

#Play Game
while not end_of_game:
    guess = input("Guess a letter. ").lower()

    # clear console after each guess
    cls()

    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"The letter {guess} is not in the chosen word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You've won!")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining. 
    print(hangman_art.stages[lives])