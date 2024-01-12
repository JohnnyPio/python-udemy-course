from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("white")
        self.penup()
        self.heading()
        self.setheading(225)
        # Consider doing x_move and y_move and using it in move and bounce

    def move(self):
        self.forward(MOVE_DISTANCE)

    def bounce(self):
        self.seth(self.heading() + 90)
