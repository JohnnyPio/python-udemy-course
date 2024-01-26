from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Timer", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    clock_min = floor(count / 60)
    count_sec = count % 60

    if 0 <= count_sec < 10:
        count_sec = f"0{count_sec}"

    if 0 <= clock_min < 10:
        clock_min = f"0{clock_min}"

    canvas.itemconfig(timer_text, text=f"{clock_min}:{count_sec}")
    if count > 0:
        window.after(1, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        checkbox_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato + Time
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 111.5, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# Timer
title_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 48, "bold"), fg=GREEN)
title_label.grid(row=0, column=1)

# Start and Reset Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=2, column=2)

# Checkbox
checkbox_label = Label(fg=GREEN, bg=YELLOW)
checkbox_label.grid(row=4, column=1)

# Reps
reps = 0

window.mainloop()
