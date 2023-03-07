from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
def move_forwards():
    tim.forward(10)

def turn_cw():
    tim.setheading(tim.heading()+10)

def turn_ccw():
    tim.setheading(tim.heading()-10)

def move_backwards():
    tim.backward(10)

def clear():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_cw)
screen.onkey(key="d", fun=turn_ccw)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(clear, "c")

screen.exitonclick()