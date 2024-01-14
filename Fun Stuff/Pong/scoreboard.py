from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_paddle_score} to {self.right_paddle_score}", align="left", font=FONT)

    def increase_left_score(self):
        self.left_paddle_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_paddle_score += 1
        self.update_scoreboard()

