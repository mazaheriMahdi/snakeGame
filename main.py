import time

from snake import Snake
from turtle import Screen

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
tom = Snake(screen)
screen.listen()
screen.onkey(tom.up, "Up")
screen.onkey(tom.down, "Down")
screen.onkey(tom.right, "Right")
screen.onkey(tom.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    tom.move()
    time.sleep(0.1)
