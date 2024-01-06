import turtle
import turtle as t
import random


tim = t.Turtle()
tim.shape("turtle")
tim.color("HotPink")
tim.shapesize(2)
#Set the global color mode
t.colormode(255)

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
    red = random.randint(0, 255)
    print(f"red = {red}")
    green = random.randint(0, 255)
    print(f"green = {green}")
    blue = random.randint(0, 255)
    print(f"blue = {blue}")
    for _ in range(num):
        tim.pencolor(red, green, blue)
        tim.forward(100)
        tim.right(360/num)


screen = t.Screen()
screen.exitonclick()
