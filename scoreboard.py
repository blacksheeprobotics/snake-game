from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto((-20, 270))
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 18, 'normal'))
