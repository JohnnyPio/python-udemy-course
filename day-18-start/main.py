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
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Draw a triangle through decagon
for num in range(3, 10+1):
    for _ in range(num):
        tim.forward(100)
        tim.right(360/num)

screen = t.Screen()
screen.exitonclick()
