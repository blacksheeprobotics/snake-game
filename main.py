import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.update()

game_is_on = True
step = 0
while game_is_on and step < 20:
    screen.update()
    time.sleep(0.1)

    snake.move()

    step += 1

screen.exitonclick()
