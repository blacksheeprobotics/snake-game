from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("game_data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.goto((-20, 270))
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Arial', 18, 'normal'))

    def reset(self):
        file = open("game_data.txt", mode="w")
        if self.score > self.high_score:
            self.high_score = self.score
            with open("game_data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            file.close()
        self.score = 0
        self.write_score()
