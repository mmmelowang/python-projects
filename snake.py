from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = [] #attribute
        self.create_snake() #这样用snake这个class做出的project自动会call create_snake function, 先写出这个function再create这个function
        self.head = self.segment[0]#attribute, we only care about what direction the first segement of the snake(head) is going

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        #identify the position to add segment
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def reset(self): #once the user games over, reset the snake body and recreate the body
        #in order to remove our previous dead snake out of the screen, loop through each segement
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segment[-1].position()) #turtule.position() is a methods from turtle class

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1): #start from position[-2] which is the last segment and go by -1
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y) #the last segment to go to the position of the second to last segment
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: #when you face a direction, you can't turn backwards
            #when the head is facing down, it doesn't allow to change direction
            #turtle. heading(): return the turtle's current direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
