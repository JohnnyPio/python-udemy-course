from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Scoreboard
        self.score_label = Label()
        self.score_label.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=("Arial", 14, "normal"),
                                justify="center", fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas_color = "white"
        self.canvas = Canvas(bg=self.canvas_color, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        button_row = 2
        self.true_button = Button()
        true_img = PhotoImage(file="images/true.png")
        self.true_button.config(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=button_row, column=0)

        self.false_button = Button()
        false_img = PhotoImage(file="images/false.png")
        self.false_button.config(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=button_row, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


