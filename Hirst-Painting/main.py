import random
import colorgram
import turtle

tim = turtle.Turtle()
turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

distance = 20
initial_x = tim.xcor()
y_change = 0
initial_y = tim.ycor()

print(initial_x)
for _ in range(10):
    # Move vertically
    tim.setx(initial_x)
    tim.sety(y_change)
    y_change += distance
    for _ in range(10):
        # Dots horizontally
        tim.penup()
        rand_color = random.choice(rgb_colors)
        tim.dot(distance, rand_color)
        tim.forward(distance)


screen = turtle.Screen()
screen.exitonclick()


