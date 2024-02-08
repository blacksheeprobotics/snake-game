from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(object):
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.snake_segments.append(segment)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading() == DOWN:
            pass
        else:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.snake_segments[0].heading() == UP:
            pass
        else:
            self.snake_segments[0].setheading(DOWN)

    def right(self):
        if self.snake_segments[0].heading() == LEFT:
            pass
        else:
            self.snake_segments[0].setheading(RIGHT)

    def left(self):
        if self.snake_segments[0].heading() == RIGHT:
            pass
        else:
            self.snake_segments[0].setheading(LEFT)
