from turtle import Turtle, Screen
import random
screen = Screen()
timmy = Turtle()
tommy = Turtle()
jimmy = Turtle()
tom = Turtle()
tim = Turtle()

timmy.color("red"), timmy.shape("turtle"), timmy.penup()
tommy.color("blue"), tommy.shape("turtle"), tommy.penup()
jimmy.color("green"), jimmy.shape("turtle"), jimmy.penup()
tom.color("yellow"), tom.shape("turtle"), tom.penup()
tim.color("purple"), tim.shape("turtle"), tim.penup()
screen.setup(width=500, height=400)



def random_distance(turtle):
    distance = random.randrange(45)
    turtle.forward(distance)


def starting_line(turtles):
    height = -140
    for turtle in turtles:
        turtle.setpos(x=-250,y=height)
        height += 70

turtles = [timmy,tommy,jimmy,tom,tim]

race_status = False
winner = ""
starting_line(turtles)
guess = screen.textinput(title="Guess", prompt="Which color turtle do you think will win?")
while not race_status:
    for turtle in turtles:
        random_distance(turtle)
        if turtle.xcor() > 240:
            race_status = True
            winner = turtle.pencolor()

if winner == guess:
    print(f"You've won the bet! Congrats the {winner} turtle won the race!")
else:
    print(f"Too bad. The {winner} turtle won this time. Try again next time.")