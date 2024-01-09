import turtle
from turtle import Screen, Turtle

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turtle setup
turtle.colormode(255)

# Initialize snake position
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.fillcolor("white")
    new_segment.goto(position)



screen.exitonclick()