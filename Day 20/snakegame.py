from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

starting =[(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

game_state = True

def up(segments):
    catchup=0
    for segment in segments:
        segment.forward(catchup)
        segment.setheading(90)
        segment.forward(20)
        catchup+=20

def left(segments):
    catchup=0
    for segment in segments:
        segment.forward(catchup)
        segment.setheading(180)
        segment.forward(20)
        catchup+=20

def down(segments):
    catchup=0
    for segment in segments:
        segment.forward(catchup)
        segment.setheading(270)
        segment.forward(20)
        catchup+=20

def right(segments):
    catchup=0
    for segment in segments:
        segment.forward(catchup)
        segment.setheading(0)
        segment.forward(20)
        catchup+=20

def direction(state):
    if state == "right":



while game_state:
    screen.update()
    time.sleep(.1)
    current_direction = "right"
    new_direction = "right"
    while new_direction == current_direction:


screen.onkey()





screen.exitonclick()
