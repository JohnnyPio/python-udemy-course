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

game_on = True
while game_on:
    # cls()
    print(art.logo)
    WIN_NUMBER = random.randint(0,100)
    user_difficulty = input(f"Select a difficulty, 'Easy' or 'Hard'. \n")
    user_guess = int(input(f"Pick a number between 1 and 100. \n"))

    def higher_or_lower(guess,actual_number):
        if guess > actual_number:
            new_guess = int(input(f"{guess} too high, select a lower number. \n"))
            return new_guess
        else:
            new_guess = int(input(f"{guess} too low, select a higher number. \n"))
            return new_guess

    number_of_tries = 0
    if user_difficulty == "Easy":
        number_of_tries = 10
    else:
        number_of_tries = 5

    while number_of_tries > 0:
        user_guess = higher_or_lower(user_guess,WIN_NUMBER)
        if user_guess == WIN_NUMBER:
            print(f"{user_guess} is correct, you win!")
            number_of_tries = 0
            game_on = False
        number_of_tries -= 1