from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial",24,"normal"))


