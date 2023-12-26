import art
import os
import random

#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# clear console setup
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
game_on = True
while game_on:
    print(art.logo)
    WIN_NUMBER = random.randint(0,100)
    user_difficulty = input(f"Select a difficulty, 'Easy' or 'Hard'. \n")

    def higher_or_lower(guess,actual_number):
        if guess > actual_number:
            new_guess = int(input(f"{guess} too high, select a lower number. \n"))
            return new_guess
        else:
            new_guess = int(input(f"{guess} too low, select a higher number. \n"))
            return new_guess

    # Set difficulty
    if user_difficulty == "Easy":
        number_of_tries = 10
    else:
        number_of_tries = 5
    print(f"You have {number_of_tries} guesses remaining!")

    # Initialize first guess
    user_guess_str = input(f"Pick a number between 1 and 100. \n")
    user_guess = int(user_guess_str)
    number_of_tries -= 1
    print(f"You have {number_of_tries} guesses remaining.")

    while number_of_tries >= 0:
        user_guess = higher_or_lower(user_guess,WIN_NUMBER)
        number_of_tries -= 1
        print(f"You have {number_of_tries} guesses remaining.")
        if user_guess == WIN_NUMBER:
            print(f"{user_guess} is correct, you win! \n")
            game_on = False
            break
        if number_of_tries == 0:
            print(f"You ran out of guesses. You lose! \n")
            game_on = False
            break