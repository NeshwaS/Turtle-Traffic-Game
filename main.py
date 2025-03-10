from turtle import Screen
from ScoreBoard import ScoreBoard
from player import Player
from carManager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_Car()
    carManager.move_cars()

    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    if player.is_at_finish_line():
        player.go_back()
        scoreboard.score()
        carManager.level_up()

screen.exitonclick()
