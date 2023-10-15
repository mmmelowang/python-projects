from turtle import Turtle
import random

class Food(Turtle): #Food is inheriting Turtle class
    def __init__(self): #food is also a Turtle object
        super().__init__()
        self.shape("circle") #change the attribute from the super(Turtle)
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        # random_x = random.randint(-280,280) #our square is 300*300, so we don't want the food to touch the boundary, so set +/-280
        # random_y = random.randint(-280, 280)
        self.refresh() # set the position by using goto(), and so Food has the attribution of position

    #create a refresh function to refresh the position of food once the snake contact food
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)

