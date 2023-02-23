# from turtle import Turtle
#
# timmy = Turtle()
# timmy = Turtle.shape("turtle")
#

import turtle as t
import random
tim=t.Turtle()
t.colormode(255)

##Square to Decagon
# colours = ["CornflowerBlue"]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

##Random Directions
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed("fastest")
def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()

