import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.onkey(player.move, "Up")
screen.listen()


def create_new_cars_with_delay():
    car_manager.add_to_car_list()
    car_manager.move_cars()


game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    if player.check_if_finished():
        scoreboard.change_label()
        car_manager.change_pace()

    create_new_cars_with_delay()
    if car_manager.check_distance(player):
        scoreboard.game_over()
        game_is_on = False


screen.listen()
screen.exitonclick()
