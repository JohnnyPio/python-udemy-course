from tkinter import *

# ---------------------------- CONSTANTS ------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Flash Card App")
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card Background
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Card Labels
current_language = "French"
language_label = canvas.create_text(400, 150, text=current_language, font=("Ariel", 40, "italic"))

current_word = "trouve"
word_label = canvas.create_text(400, 263, text=current_word, font=("Ariel", 60, "bold"))

# Buttons
button_row = 1
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=button_row, column=0, sticky="EW")

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=button_row, column=1, sticky="EW")

window.mainloop()
