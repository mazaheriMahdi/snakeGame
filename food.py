import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        super().shape("circle")
        super().color("blue")
        super().penup()
        super().shapesize(0.5)
        super().speed("fastest")
        self.eat()

    def eat(self):
        super().goto(random.randint(-250, 250), random.randint(-250, 250))
