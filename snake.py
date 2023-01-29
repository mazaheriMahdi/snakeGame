from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self, screen):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segment_list = []
        self.screen = screen

        for i in self.starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)
            self.segment_list.append(new_segment)
        self.head = self.segment_list[0]
        screen.update()

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            x = self.segment_list[i - 1].xcor()
            y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
