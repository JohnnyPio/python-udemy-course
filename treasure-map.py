line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
split_position = list(position)
row_number_str = split_position[1]
row_number = int(row_number_str)
print(row_number)
col_letter = split_position[0]
col_number = 0

if col_letter == "A":
  col_number = 0
elif col_letter == "B":
  col_number = 1
elif col_letter == "C":
  col_number = 2
else:
  print("Column Error.")
print(col_number)

if row_number == 1:
  line1.pop(col_number)
  line1.insert(col_number, "X")
if row_number == 2:
  line2.pop(col_number)
  line2.insert(col_number, "X")
if row_number == 3:
  line3.pop(col_number)
  line3.insert(col_number, "X")

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
