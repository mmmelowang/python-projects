from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #turn turtle animation on/off, default to 1(not update), here it is 0 which will update the screen

#initalize snake and food objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard() #show the scoreboard first

#control the snake
screen.listen()
screen.onkey(snake.up, "Up") #those are the keys that it will detect, once that detected, it will call
#the corresponding methods within snake class
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() #here we need to update the screen
    time.sleep(0.1)

    snake.move() #after all segments of snake move, we update the screen

    #detecting when the snake contact the food and tell the food to move to a new random location
    #use the turtle.distance()function within turtle class, basically it measure the distance between the turtle and the object located in (x,y)
    if snake.head.distance(food) <= 15: #we set 15 because the food's diameter is 10
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False #then going to add game_over methods in scoreboard
        scoreboard.reset()
        snake.reset()

    #detect collision with its own body
    for segment in snake.segment:
        if segment == snake.head:#bypass the head of the snake
            pass
        elif snake.head.distance(segment) < 10: #those two are not independent
            game_is_on = False
            scoreboard.update_scoreboard()
            snake.reset()


screen.exitonclick()