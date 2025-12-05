# Annabelle's code

import turtle
import tkinter as tk

win = turtle.Screen()

main = tk.Tk()
canvas = tk.Canvas(main, width = 600, height = 600)


def draw_face(color):
    face_turt = turtle.Turtle()
    face_turt.speed(0)
    face_turt.hideturtle()
    face_turt.penup()
    face_turt.goto(0, -150)
    face_turt.pendown()
    # set turtle color to inputted color
    face_turt.pencolor(color)
    face_turt.fillcolor(color)
    face_turt.begin_fill()
    # draw face
    for x in range(2):
        face_turt.circle(120, 45)
        face_turt.circle(200, 90)
        face_turt.circle(120, 45)
    face_turt.end_fill()
    # go back to center
    face_turt.penup()
    face_turt.goto(0,0)
    face_turt.pendown()

def draw_eyes(color):
    eyes_turt = turtle.Turtle()
    eyes_turt.speed(0)
    eyes_turt.penup()
    eyes_turt.left(90)
    eyes_turt.forward(60)
    eyes_turt.right(90)
    eyes_turt.forward(20)
    eyes_turt.pendown()
    eyes_turt.fillcolor("white")
    eyes_turt.begin_fill()
    eyes_turt.right(50)
    eyes_turt.circle(70, 100)
    eyes_turt.left(80)
    eyes_turt.circle(70, 100)
    eyes_turt.end_fill()
    eyes_turt.penup()
    eyes_turt.right(50)
    eyes_turt.back(55)
    eyes_turt.dot(45, color)
    eyes_turt.dot(20, "black")
    eyes_turt.penup()
    eyes_turt.forward(90)
    eyes_turt.pendown()
    eyes_turt.fillcolor("white")
    eyes_turt.begin_fill()
    eyes_turt.right(50)
    eyes_turt.circle(70, 100)
    eyes_turt.left(80)
    eyes_turt.circle(70, 100)
    eyes_turt.end_fill()
    eyes_turt.penup()
    eyes_turt.right(50)
    eyes_turt.back(55)
    eyes_turt.dot(45, color)
    eyes_turt.dot(20, "black")

def face1():
    draw_face("brown")

def face2():
    draw_face("pink")

def face3():
    draw_face("light blue")

eyebrow_turt = turtle.Turtle()
eyebrow_turt.color("black")
eyebrow_turt.hideturtle()
# move to position
eyebrow_turt.penup()
eyebrow_turt.goto(-100, 60)
eyebrow_turt.pendown()
eyebrow_turt.circle(50, 100)

face_frame = tk.Frame(main)
face_frame.pack(pady = 10)

tk.Button(face_frame, text = "1", command = face1, width = 10).grid(row = 0, column = 0, padx = 5)
tk.Button(face_frame, text = "2", command = face2, width = 10).grid(row = 0, column = 2, padx = 5)
tk.Button(face_frame, text = "3", command = face3, width = 10).grid(row = 0, column = 3, padx = 5)





win.exitonclick()
