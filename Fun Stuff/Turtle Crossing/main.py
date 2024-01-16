import random
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()
scoreboard = Scoreboard()
my_cars = CarManager()

screen.listen()
screen.onkey(my_turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(my_cars.move_speed)
    screen.update()
    my_cars.create_car()
    my_cars.move_cars()

    # Increment level, reset turtle position, speed up cars at the top
    if my_turtle.ycor() >= FINISH_LINE_Y:
        my_turtle.reset_position()
        scoreboard.increase_level()
        my_cars.move_speed *= 0.9

    # Collision detection
    for car in my_cars.all_cars:
        if car.distance(my_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
