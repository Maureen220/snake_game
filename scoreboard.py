from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("#3b5d05")
        self.write(f"Score: {self.score}", move=False, align='center', font=('Impact', 15, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align='center', font=('Impact', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Impact', 15, 'normal'))