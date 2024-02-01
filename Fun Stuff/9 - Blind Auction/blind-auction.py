import os
import art

# clear console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Intro
print(art.logo)
print("Welcome to the secret auction program.")

def pick_winner(dictionary):
    highest_bid = 0
    winner = ""
    for key in dictionary:
        if dictionary[key] > highest_bid:
            highest_bid = dictionary[key]
            winner = key
    print(f"The winner is {winner} with a bid of {highest_bid}")

other_bidders = True
names_and_bids_dict = {}
while other_bidders == True:
    user_name = input("What is your name?\n")
    user_bid = int(input("What is your bid?\n"))
    names_and_bids_dict[user_name] = user_bid

    other_bidders_input = input(f"Are there any other bidders? Type {'yes'} or {'no'}.\n")
    if other_bidders_input == "yes":
        cls()
    elif other_bidders_input == "no":
        pick_winner(names_and_bids_dict)
        other_bidders = False
    else:
        other_bidders_input = input(f"Invalid answer, please choose either {'yes'} or {'no'}!\n")

