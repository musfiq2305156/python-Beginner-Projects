###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

#print(rgb_colors)
from turtle import Turtle,Screen
import random
dhon=Turtle()
screen=Screen()
screen.colormode(255)
dhon.shape("arrow")
#dhon.color("lime")
dhon.speed(20)
y=0.00
for i in range(10):
    dhon.penup()
    dhon.goto(0,y)
    dhon.pendown()
    
    for j in range(10):
        x=random.choice(rgb_colors)
        dhon.color(x)
        dhon.dot(10,x)
        dhon.penup()
        dhon.forward(30)
        dhon.pendown()
    y+=30



screen.exitonclick()