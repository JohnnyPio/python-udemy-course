from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.fillcolor("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(STARTING_POSITION[0], new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
