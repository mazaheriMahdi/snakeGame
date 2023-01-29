from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        super().penup()
        super().goto(0 , 270)
        super().pencolor("white")
        super().hideturtle()
        self.write()

    def write(self):
        super().clear()
        super().write(arg=f"Score : {self.score}", move=False, align="center" , font=("Arial" , 17 , "bold"))

    def gameOver(self):

        super().goto(0,0)
        super().write(arg=f"GAME OVER", move=False, align="center" , font=("Arial" , 19 , "bold"))

    def addScore(self):
        self.score += 1
