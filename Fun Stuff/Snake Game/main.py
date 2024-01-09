import turtle
from turtle import Screen, Turtle
from snake import Snake
import time

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Turtle setup
turtle.colormode(255)
turtle.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

screen.exitonclick()
