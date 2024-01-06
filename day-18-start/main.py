import turtle
import turtle as t


tim = t.Turtle()
tim.shape("turtle")
tim.color("HotPink")
tim.shapesize(2)

# Draw a Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a Dashed Line
for _ in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()
