import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

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

# Initialize paddles and ball
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()

# Need a way to identy left/right boundaries so scoring will count

# Listeners for paddles
screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Bounce off top and bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.wall_bounce()

    # Detect collision with right paddle and bounce
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()

    # Detect collision with left paddle and bounce
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()




# Create a class for the scoreboard

screen.exitonclick()
