from tkinter import *

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

# Email/Username Line
email_username_row = website_row + 1
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=email_username_row, column=0)

email_username_input = Entry(width=35)
email_username_input.grid(row=email_username_row, column=1, columnspan=2, sticky="EW")

# Password Line
password_row = website_row + 2
password_label = Label(text="Password:")
password_label.grid(row=password_row, column=0)

password_input = Entry(width=21)
password_input.grid(row=password_row, column=1, sticky="EW")

password_button = Button(text="Generate Password")
password_button.grid(row=password_row, column=2)

# Add
add_row = website_row + 3
add_button = Button(text="Add", width=36)
add_button.grid(row=add_row, column=1, columnspan=2, sticky="EW")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()
