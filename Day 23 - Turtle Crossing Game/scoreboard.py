from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.name = 'Level:'
        self.level_no = 0


    def point_increase(self):
        self.level_no += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(self.name, align='center', font=FONT)
        self.goto(-120, 200)
        self.write(self.level_no, align='center', font=FONT)
