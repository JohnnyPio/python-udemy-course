import turtle
from turtle import Screen, Turtle
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turtle setup
turtle.colormode(255)
turtle.tracer(0)

# Initialize snake position
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.fillcolor("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg_num in range(len(segments)-1, 0, -1):
        prior_segment = segments[seg_num-1]
        segments[seg_num].goto(prior_segment.xcor(), prior_segment.ycor())
    segments[0].forward(20)

screen.exitonclick()