from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


def read_high_score():
    with open("data.txt") as file:
        contents = int(file.read())
        return contents


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
