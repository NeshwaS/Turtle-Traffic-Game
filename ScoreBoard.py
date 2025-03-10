from turtle import Turtle
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"level:{self.level}", align="left", font=FONT)

    def score(self):
        self.level += 1
        self.update_scoreboard()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)


