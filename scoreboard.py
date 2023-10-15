from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal") #in the future if I want to change, I don't need to dig through my codes below

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #open data.txt and find the high score
        with open("data.txt") as file:
            self.high_score = int(file.read())
        #self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)#move to the top before we write
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) #need to adjust the color before showing it


    def update_scoreboard(self):
            self.clear()
            self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self): #store the high score and reset score
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt",mode="w") as file: #write to the high score
            file.write(f"{self.high_score}") #write in format of a string, not a number

        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("game over", align = ALIGNMENT, font = FONT)