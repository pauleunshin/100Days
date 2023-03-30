from turtle import Screen, Turtle
from mysnake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

game_state = True
snake = Snake()

###This does not work
# def up(segments):
#     current_pos=[]
#     heading = 0
#     for segment in segments:
#         if not current_pos:
#             segment.setheading(90)
#             segment.forward(20)
#             current_pos=[segment.xcor,segment.ycor]
#             set_heading
#         else:
#             segment.setpos(current_pos)
#             segment.setheading
#
# def left(segments):
#     catchup=0
#     for segment in segments:
#         segment.forward(catchup)
#         segment.setheading(180)
#         segment.forward(20)
#         catchup+=20
#
# def down(segments):
#     catchup=0
#     for segment in segments:
#         segment.forward(catchup)
#         segment.setheading(270)
#         segment.forward(20)
#         catchup+=20
#
# def right(segments):
#     catchup=0
#     for segment in segments:
#         segment.forward(catchup)
#         segment.setheading(0)
#         segment.forward(20)
#         catchup+=20

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_state:
    screen.update()
    time.sleep(.1)
    snake.move()


screen.onkey()
screen.exitonclick()
