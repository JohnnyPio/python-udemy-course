import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)
is_race_on = False
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race. Enter a color of either: "
                                                           "red, orange, yellow, green, blue, or purple.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

if user_bet:
    is_race_on = True

starting_x = -width/2 + (width/20)
starting_y = -height/2 + (height/12)

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(starting_x, starting_y)
    starting_y += height/6
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= (width/2 - 5):
            is_race_on = False
            print(f"The {turtle.fillcolor()} turtle won!")
            if user_bet.lower() == turtle.fillcolor():
                print("You bet correctly!")
            else:
                print("You bet incorrectly.")
            break

# Close screen on click
screen.exitonclick()
