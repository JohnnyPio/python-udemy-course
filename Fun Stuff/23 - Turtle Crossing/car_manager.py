from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.move_speed = 0.1
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.fillcolor(random.choice(COLORS))
            new_car.setx(300)
            random_y = random.randrange(-250, 250, 20)
            new_car.sety(random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            car.goto(new_x, car.ycor())


    # def next_level_faster(self):
    #     STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
