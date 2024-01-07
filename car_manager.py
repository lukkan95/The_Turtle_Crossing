from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_list = []
        self.current_pace = STARTING_MOVE_DISTANCE

    def change_pace(self):
        for elem in self.car_list:
            elem.pace += MOVE_INCREMENT
        self.current_pace += MOVE_INCREMENT

    def add_to_car_list(self):
        if random.randint(1, 7) == 6:
            self.car_list.append(Car(self.current_pace))

    def move_cars(self):
        for car in self.car_list:
            car.move()

    def check_distance(self, elem):
        for car in self.car_list:
            if car.distance(elem) < 20:
                return True


class Car(Turtle):
    def __init__(self, pace):
        super().__init__()
        self.shape('square')
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.speed("fastest")
        self.color(random.choice(COLORS))
        self.left(180)
        self.goto(300, random.randint(-240, 240))
        self.pace = pace

    def move(self):
        self.forward(self.pace)

    # def change_peace_of_car(self):
    #     self.pace += MOVE_INCREMENT

