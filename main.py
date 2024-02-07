import turtle
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    snake_limb = turtle.Turtle("square")
    snake_limb.penup()
    snake_limb.color("white")
    snake_limb.goto(position)
    snake_segments.append(snake_limb)
screen.update()

game_is_on = True
step = 0
while game_is_on and step < 20:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(snake_segments)-1, 0, -1):
        new_x = snake_segments[seg_num - 1].xcor()
        new_y = snake_segments[seg_num - 1].ycor()
        snake_segments[seg_num].goto(new_x, new_y)
    snake_segments[0].forward(10)
    snake_segments[0].left(90)

    step += 1

screen.exitonclick()
