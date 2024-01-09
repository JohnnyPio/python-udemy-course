import turtle
from turtle import Screen, Turtle

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turtle setup
turtle.colormode(255)

# Initialize snake parts
snake_parts = []


segment_1 = Turtle()
segment_1.penup()
segment_1.fillcolor("white")
segment_1.shape("square")
initial_x = segment_1.xcor()
initial_y = segment_1.xcor()

segment_2 = Turtle()
segment_2.penup()
segment_2.fillcolor("white")
segment_2.shape("square")
segment_2.setx(initial_x - 20)

segment_3 = Turtle()
segment_3.penup()
segment_3.fillcolor("white")
segment_3.shape("square")
segment_3.setx(segment_2.xcor() - 20)




screen.exitonclick()