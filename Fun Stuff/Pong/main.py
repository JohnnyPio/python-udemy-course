import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

# Listeners for paddles
screen.listen()
screen.onkey(left_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "w")
screen.onkey(right_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Bounce off top and bottom wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with right or left paddle and bounce
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340
            or ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Detect miss with right paddle, increase score
    if ball.distance(right_paddle) >= 50 and ball.xcor() > 340:
        scoreboard.increase_left_score()
        ball.reset_position()

    # Detect miss with left paddle, increase score
    if ball.distance(left_paddle) >= 50 and ball.xcor() < -340:
        scoreboard.increase_right_score()
        ball.reset_position()

screen.exitonclick()
