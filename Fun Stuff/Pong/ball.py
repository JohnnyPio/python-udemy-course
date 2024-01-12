from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.fillcolor("white")
        self.goto(0, 400)
        self.setheading(225)


    # def bounce(self):
