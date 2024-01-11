import turtle
from turtle import Screen, Turtle
from paddle import Paddle

# Create the screen, black background
screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong")

# Turtle setup
turtle.colormode(255)
turtle.tracer(0)

# Initialize
#left_paddle = Paddle().create_left_paddle()

# Need a way to identify top/bot boundaries so ball will bounce
# Need a way to identy left/right boundaries so scoring will count

# Create a class for the paddles
screen.listen()
# screen.onkey(left_paddle.move_up, "Up")
# screen.onkey(left_paddle.move_down, "Down")
# Need a way to bounce ball off paddle

# Create a class for the ball

# Create a class for the scoreboard

screen.exitonclick()
