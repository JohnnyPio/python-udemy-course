from turtle import Turtle, Screen

screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race. Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

starting_x = -width/2 + (width/20)
starting_y = -height/2 + (height/12)

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(starting_x, starting_y)
    starting_y += height/6

screen.exitonclick()
