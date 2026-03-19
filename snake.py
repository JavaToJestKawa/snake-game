from turtle import Turtle, Screen
import time

INITIAL_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = int(20)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.blocked = False
        self.head = self.segments[0]

    def create(self):
        for coordinate in INITIAL_COORDINATES:
            self.add_segment(coordinate)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # if not self.blocked:
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
                # self.blocked = True

    def down(self):
        # if not self.blocked:
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
                # self.blocked = True

    def left(self):
        # if not self.blocked:
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
                # self.blocked = True

    def right(self):
        # if not self.blocked:
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
                # self.blocked = True

    def release (self):
        self.blocked = False

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create()
        self.head = self.segments[0]
