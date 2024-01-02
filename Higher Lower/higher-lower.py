import os
import random
import art
import game_data

# Initialize new list of remaining samples
remaining_samples = game_data.data
# num_of_rems = len(remaining_samples)
# print(num_of_rems)

# Get first random item from data
first_item = random.choice(game_data.data)

# Delete the entry from data
remaining_samples.remove(first_item)

# Get second entry from data
second_item = random.choice(remaining_samples)

# Delete that entry
remaining_samples.remove(second_item)

# Prompt user which of the entries has a higher follower count
def compare(fir_item,sec_item):
    print(f"Compare A: {fir_item['name']}, a {fir_item['description']}, from {fir_item['country']}.")
    print(art.vs)   
    print(f"Compare B: {sec_item['name']}, a {sec_item['description']}, from {sec_item['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B':")
    if fir_item['follower_count'] > sec_item['follower_count'] and choice == "A":
        print("Correct")
    elif fir_item['follower_count'] < sec_item['follower_count'] and choice == "B":
        print("Correct")
    else:
        print("You lose.")

compare(first_item,second_item)

# If wrong, you lose

# (Loop) If right, pull next entry from data and remove from list

# "Compare A: name, a description, from country"