from turtle import Turtle,Screen,listen
import time
screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
turtles=[Turtle() for _ in range(3)]
for i in range(3):
    turtles[i].shape("square")
    turtles[i].color("purple")
    turtles[i].penup()
    turtles[i].goto(x=-20*i,y=0)
listen()
def move_up():
    heading = turtles[0].heading()
    if heading==0:
        turtles[0].left(90)
    elif heading==180:
        turtles[0].right(90)
def move_down():
    heading = turtles[0].heading()
    if heading==0:
        turtles[0].right(90)
    elif heading==180:
        turtles[0].left(90)
def move_left():
    heading = turtles[0].heading()
    if heading==90:
        turtles[0].left(90)
    elif heading==270:
        turtles[0].right(90)
def move_right():
    heading = turtles[0].heading()
    if heading==90:
        turtles[0].right(90)
    elif heading==270:
        turtles[0].left(90)
def pause():
    global game_on
    game_on = not game_on
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(pause, "p")
game_on = False  # Start paused

while True:
    screen.update()
    time.sleep(0.15)
    if game_on:
        # Store current positions of all segments
        positions = [(t.xcor(), t.ycor()) for t in turtles]
        turtles[0].forward(20)
        for i in range(1, len(turtles)):
            turtles[i].goto(positions[i-1])
screen.exitonclick()