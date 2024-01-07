import turtle
import turtle as t
import random


tim = t.Turtle()
tim.shape("turtle")
tim.color("HotPink")
tim.shapesize(3)
#Set the global color mode
t.colormode(255)
#Use a thicker line size
tim.pensize(20)
#Move faster
tim.speed(10)

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
# for num in range(3, 10+1):
#     red = random.randint(0, 255)
#     print(f"red = {red}")
#     green = random.randint(0, 255)
#     print(f"green = {green}")
#     blue = random.randint(0, 255)
#     print(f"blue = {blue}")
#     for _ in range(num):
#         tim.pencolor(red, green, blue)
#         tim.forward(100)
#         tim.right(360/num)

# Draw a random walk with random colors
turn_angles = [0, 90, 180, 270]
for _ in range(200):
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(rand_color)
    tim.left(random.choice(turn_angles))
    tim.forward(50)

screen = t.Screen()
screen.exitonclick()
