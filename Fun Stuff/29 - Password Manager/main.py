from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_to_file():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                updated_data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data
            updated_data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(updated_data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Lock image
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website Line
website_row = 1
website_label = Label(text="Website:")
website_label.grid(row=website_row, column=0)

website_input = Entry(width=35)
website_input.grid(row=website_row, column=1, columnspan=2, sticky="EW")
website_input.focus()

# Email/Username Line
email_username_row = website_row + 1
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=email_username_row, column=0)

email_username_input = Entry(width=35)
email_username_input.grid(row=email_username_row, column=1, columnspan=2, sticky="EW")
email_username_input.insert(END, "john.s.piotrowski@gmail.com")

# Password Line
password_row = website_row + 2
password_label = Label(text="Password:")
password_label.grid(row=password_row, column=0)

password_input = Entry(width=21)
password_input.grid(row=password_row, column=1, sticky="EW")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=password_row, column=2)

# Add
add_row = website_row + 3
add_button = Button(text="Add", width=36, command=add_to_file)
add_button.grid(row=add_row, column=1, columnspan=2, sticky="EW")

window.mainloop()
