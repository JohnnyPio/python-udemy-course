line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# This grabs the first element of the user input, the letter, and makes it lowercase
letter = position[0].lower()

# This is a comparative list of letter options
abc = ["a", "b", "c"]

# This assigns an index number to the letter users entered
letter_index = abc.index(letter)

# This assigns an index number to the number users entered
number_index = int(position[1]) - 1

# This reassigns X using list-of-lists
map[number_index][letter_index] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
