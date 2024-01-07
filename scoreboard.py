from turtle import Turtle

FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Level: {self.level}", font=FONT, align="CENTER")

    def add_level(self):
        self.level += 1

    def change_label(self):
        self.add_level()
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="CENTER")

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.write(f"Game over.", move=False, align="center", font=FONT)