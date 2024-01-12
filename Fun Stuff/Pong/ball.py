from turtle import Turtle

MOVE_DISTANCE = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("white")
        self.penup()
        self.setheading(225)

    def move(self):
        self.forward(MOVE_DISTANCE)

    # def bounce(self):
    #     self.setheading(45)
