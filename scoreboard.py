from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.hideturtle()
        self.goto(0, 265)
        self.color("blue")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score}        HIGH_SCORE: {self.high_score}", False, align=ALLIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                contents = file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
