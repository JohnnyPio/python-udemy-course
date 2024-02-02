from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Scoreboard
        self.scoreboard = Label()
        self.score = 0
        self.scoreboard.config(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Arial", 14, "normal"),
                               justify="center", fg="white")
        self.scoreboard.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        button_row = 2
        self.true_button = Button()
        true_img = PhotoImage(file="images/true.png")
        self.true_button.config(image=true_img, highlightthickness=0)
        self.true_button.grid(row=button_row, column=0)

        self.false_button = Button()
        false_img = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_img, highlightthickness=0)
        self.false_button.grid(row=button_row, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
