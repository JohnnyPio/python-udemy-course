from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
initial_x = tim.xcor()
initial_y = tim.ycor()
initial_heading = tim.heading()

distance = 10
turn_angle = 10

def move_forwards():
    tim.forward(distance)


def move_backwards():
    tim.back(distance)


def turn_left():
    new_heading = tim.heading() + turn_angle
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - turn_angle
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="Escape", fun=clear)
screen.exitonclick()
