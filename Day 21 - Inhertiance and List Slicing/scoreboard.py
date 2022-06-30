from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.setposition(-30, 260)
        self.write(f"Score = {self.score}", False, align='center', font=('Arial', 15, 'bold'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False, align='center', font=('Arial', 15, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", True, align='center', font=('Arial', 15, 'bold'))

# class ScoreCount(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.color('white')
#         self.hideturtle()
#         self.setposition(20, 260)
#         self.score_count = 0
#
#     def write_score(self):
#         self.write(self.score_count, False, align='center', font=('Arial', 15, 'bold'))
#
