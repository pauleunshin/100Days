STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for segment in self.segments:
            if not current_pos:
                segment.setheading(90)
                segment.forward(20)
                current_pos = [segment.xcor, segment.ycor]
                set_heading
            else:
                segment.setpos(current_pos)
                segment.setheading

