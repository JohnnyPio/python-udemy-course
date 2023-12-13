import random
import itertools

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
computer_choice = random.randint(0,2)

user_choice_str = input()
user_choice = int(user_choice_str)

rps = [rock, paper, scissors]

print(rps[user_choice])
print("You chose:")

print(rps[computer_choice])
print("Computer chose:")

lose = "You lose."
win = "You win."
tie = "You tie."

# rock vs. paper
if user_choice == 0 and computer_choice == 1:
    print(lose)
# rock vs. scissors
elif user_choice == 0 and computer_choice == 2:
    print(win)
# paper vs. rock
elif user_choice == 1 and computer_choice == 0:
    print(win)
# paper vs. scissors
elif user_choice == 1 and computer_choice == 2:
    print(lose)
# scissors vs. rock
elif user_choice == 2 and computer_choice == 0:
    print(lose)
# scissors vs. paper
elif user_choice == 2 and computer_choice == 1:
    print(win)
else:
    print(tie)
    


