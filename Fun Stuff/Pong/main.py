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

# Initialize paddles
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

# Need a way to identify top/bot boundaries so ball will bounce
# Need a way to identy left/right boundaries so scoring will count

screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
# Need a way to bounce ball off paddle

game_is_on = True
while game_is_on:
    screen.update()


# Create a class for the ball

# Create a class for the scoreboard

screen.exitonclick()
