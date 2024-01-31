from tkinter import *
import random
import pandas
import time

# ---------------------------- CONSTANTS ------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
LEARNING_LANGUAGE = "French"
NATIVE_LANGUAGE = "English"

imported_data = pandas.read_csv("data/french_words.csv")
to_learn = imported_data.to_dict(orient="records")
learned = {}
current_card = {}


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

def remove_card():
    # if text isn't starter text

    # when green button is pressed, remove it from to_learn and move it to learned

    # print new CSV

# need to check if new CSV exists


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
card_language = canvas.create_text(400, 150, text="Press Button to Start", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

# Buttons
button_row = 1
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=get_next_card)
wrong_button.grid(row=button_row, column=0, sticky="EW")

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=get_next_card)
right_button.grid(row=button_row, column=1, sticky="EW")

window.mainloop()
