from src.wa.member1 import *
from src.wa.member2 import *
from src.wa.member3 import *

import turtle

win = turtle.Screen()
turt = turtle.Turtle()



def draw_face(color):
    # move turtle to position to start drawing face
    turt.hideturtle()
    turt.penup()
    turt.right(90)
    turt.forward(150)
    turt.left(90)
    turt.pendown()
    # set turtle color to inputted color
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
    # draw face
    for x in range(2):
        turt.circle(120, 45)
        turt.circle(200, 90)
        turt.circle(120, 45)
    turt.end_fill()
    # go back to center
    turt.penup()
    turt.goto(0,0)
    turt.pendown()



draw_face("green")

turt.penup()
turt.left(90)
turt.forward(100)
turt.right(90)

turt.fillcolor("white")
turt.begin_fill()
turt.right(50)
turt.circle(100, 100)
turt.left(80)
turt.circle(100, 100)
turt.end_fill()

win.exitonclick()
