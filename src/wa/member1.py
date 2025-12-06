# Annabelle's code

import turtle
import tkinter as tk

win = turtle.Screen()
eyebrow_turt = turtle.Turtle()

eyes_turt = turtle.RawTurtle(win)
eyes_turt.speed(0)
eyes_turt.hideturtle()

eyebrow_turt = turtle.RawTurtle(win)
eyebrow_turt.color("black")
eyebrow_turt.width(8)
eyebrow_turt.speed(0)
eyebrow_turt.hideturtle()

def draw_eyes(color):
    eyes_turt.penup()
    eyes_turt.goto(20, 60)
    eyes_turt.pendown()
    eyes_turt.fillcolor("white")
    eyes_turt.begin_fill()
    eyes_turt.right(50)
    eyes_turt.circle(60, 100)
    eyes_turt.left(80)
    eyes_turt.circle(60, 100)
    eyes_turt.end_fill()
    eyes_turt.penup()
    eyes_turt.goto(65, 60)
    eyes_turt.dot(40, color)
    eyes_turt.dot(20, "black")
    eyes_turt.setheading(180)
    eyes_turt.penup()
    eyes_turt.forward(90)
    eyes_turt.pendown()
    eyes_turt.fillcolor("white")
    eyes_turt.begin_fill()
    eyes_turt.right(50)
    eyes_turt.circle(60, 100)
    eyes_turt.left(80)
    eyes_turt.circle(60, 100)
    eyes_turt.end_fill()
    eyes_turt.penup()
    eyes_turt.goto(-70, 60)
    eyes_turt.dot(40, color)
    eyes_turt.dot(20, "black")


def draw_eyes_blue():
    draw_eyes("light blue")

def draw_eyes_green():
    draw_eyes("#92b092")

def draw_eyes_brown():
    draw_eyes("#73491c")

def draw_eyes_hazel():
    draw_eyes("#967b51")

def eyebrow_raised():
    eyebrow_turt.penup()
    eyebrow_turt.goto(115, 100)
    eyebrow_turt.setheading(130)
    eyebrow_turt.pendown()
    eyebrow_turt.circle(50, 100)
    eyebrow_turt.setheading(180)
    eyebrow_turt.penup()
    eyebrow_turt.forward(70)
    eyebrow_turt.setheading(130)
    eyebrow_turt.pendown()
    eyebrow_turt.circle(50, 100)

def eyebrow_angry():
    eyebrow_turt.penup()
    eyebrow_turt.goto(110, 115)
    eyebrow_turt.setheading(200)
    eyebrow_turt.pendown()
    eyebrow_turt.forward(70)
    eyebrow_turt.setheading(180)
    eyebrow_turt.penup()
    eyebrow_turt.forward(80)
    eyebrow_turt.setheading(160)
    eyebrow_turt.pendown()
    eyebrow_turt.forward(70)

def eyebrow_neutral():
    eyebrow_turt.penup()
    eyebrow_turt.goto(110, 115)
    eyebrow_turt.setheading(180)
    eyebrow_turt.pendown()
    eyebrow_turt.forward(70)
    eyebrow_turt.penup()
    eyebrow_turt.forward(70)
    eyebrow_turt.pendown()
    eyebrow_turt.forward(70)

draw_eyes("pink")
win.exitonclick()