from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? enter a color: ")
turtles = [Turtle() for _ in range(6)]
turtle_colors=["red","orange","cyan","green","blue","magenta"]
for i in range (6):
    turtles[i].color(turtle_colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-210,y=-100+i*40)
    turtles[i].shape("turtle")
win =False
def move_turtle(turtle):
    turtle.forward(random.randrange(10,16,4))
def finish(turtle):
    if turtle.xcor()>=210:
        return True
    return False
while not win:
    for turtle in turtles:
        move_turtle(turtle)
        if finish(turtle):
            win = True
            winner=turtle.pencolor()
            break
if winner.lower() == user_bet.lower():
    print(f"You win! The {winner} turtle is the winner!")
else:
    print(f"You lose! The {winner} turtle is the winner!")
screen.bye()

