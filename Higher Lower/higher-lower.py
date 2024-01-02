import os
import random
import art
import game_data

# define clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



# Print account data
def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# Prompt user which of the entries has a higher follower count
def check_answer(choice,first_item_followers,second_item_followers):
    """Take the user guess and follower account numbers and return whether it's correct"""
    if first_item_followers > second_item_followers and choice == "A":
        return True
    elif first_item_followers < second_item_followers and choice == "B":
        return True
    else:
        return False

def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    first_item = random.choice(game_data.data)
    second_item = random.choice(game_data.data)

    while game_should_continue:  
        first_item = second_item
        second_item = random.choice(game_data.data)

        while first_item == second_item:
            second_item = random.choice(game_data.data)

        print(f"Compare A: {format_data(first_item)}")
        print(art.vs)   
        print(f"Compare B: {format_data(second_item)}")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Follower data
        first_item_followers = first_item["follower_count"]
        second_item_followers = second_item["follower_count"]
        is_correct = check_answer(choice, first_item_followers, second_item_followers)

        if is_correct:
            score += 1
            print("Correct")
            print(f"Current Score = {score}")
        else:
            game_should_continue = False
            print("You lose.")
            print(f"Final Score = {score}")

game()