import os
import random
import art
import game_data

# define clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Initialize new list of remaining samples
remaining_samples = game_data.data
# num_of_rems = len(remaining_samples)
# print(num_of_rems)

# Prompt user which of the entries has a higher follower count
def compare(fir_item,sec_item):
    print(f"Compare A: {fir_item['name']}, a {fir_item['description']}, from {fir_item['country']}.")
    print(art.vs)   
    print(f"Compare B: {sec_item['name']}, a {sec_item['description']}, from {sec_item['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B':")
    if fir_item['follower_count'] > sec_item['follower_count'] and choice == "A":
        print("Correct")
        return fir_item
    elif fir_item['follower_count'] < sec_item['follower_count'] and choice == "B":
        print("Correct")
        return sec_item
    else:
        print("You lose.")
        return False

# clear console and print logo after each game
cls()
print(art.logo)

# Get first random item from data and delete entry
first_item = random.choice(game_data.data)
remaining_samples.remove(first_item)

# Get second entry from data and delete entry
second_item = random.choice(remaining_samples)
remaining_samples.remove(second_item)

# Get initial guess
guess_check = compare(first_item,second_item)

# (Loop) If right, pull next entry from data and remove from list
while guess_check != False:
    new_item = random.choice(game_data.data)
    remaining_samples.remove(new_item)

    new_guess_check = compare(guess_check, new_item)

    # Compare those two
    if guess_check == False:
        break
