import csv
from tkinter import *
import random
import pandas

# ---------------------------- CONSTANTS ------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
LEARNING_LANGUAGE = "French"
NATIVE_LANGUAGE = "English"
to_learn = {}
current_card = {}

try:
    imported_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = imported_data.to_dict(orient="records")


# ---------------------------- PICK WORDS ------------------------------ #


def get_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(card_language, text=LEARNING_LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[LEARNING_LANGUAGE], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(card_language, text=NATIVE_LANGUAGE, fill="white")
    canvas.itemconfig(card_word, text=current_card[NATIVE_LANGUAGE], fill="white")


def is_known():
    to_learn.remove(current_card)
    to_learn_df = pandas.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    get_next_card()


# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Flash Card App")
window.config(width=900, height=626, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Card Background
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

# Card Labels TODO - clean this initializer up
card_language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

# Buttons
button_row = 1
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=get_next_card)
wrong_button.grid(row=button_row, column=0, sticky="EW")

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
correct_button.grid(row=button_row, column=1, sticky="EW")

# Initialize cards
get_next_card()

window.mainloop()
