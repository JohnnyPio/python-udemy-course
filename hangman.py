import random

# Stage ASCII art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Variables
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
end_of_game = False
lives = 6

#Testing code
print(f"pssst, the solution is {chosen_word}")

#Create blanks
display = []
for char in chosen_word:
    display += "_"

#Play Game
while not end_of_game:
    guess = input("Guess a letter. ").lower()

    #Check guessed letter
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if chosen_word.find(guess) == -1:
        lives -= 1
    
    if lives == 0:
        end_of_game = True
        print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You've won!")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])