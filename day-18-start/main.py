from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("HotPink")
tim.shapesize(5)

# Draw a Square
for num in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
