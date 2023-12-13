#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rand_letters = random.choices(letters,k = nr_letters)
rand_symbols = random.choices(symbols,k = nr_symbols)
rand_numbers = random.choices(numbers,k = nr_numbers)

full_list = rand_letters + rand_symbols + rand_numbers

easy_list_as_text = ""
for item in full_list:
    easy_list_as_text += item
print(f"The easy way: {easy_list_as_text}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_list = full_list
random.shuffle(hard_list)

hard_list_as_text = ""
for item in hard_list:
    hard_list_as_text += item

print(f"The hard way: {hard_list_as_text}")