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
    #eyes_turt.left(90)
    #eyes_turt.forward(60)
    #eyes_turt.right(90)
    #eyes_turt.forward(20)
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

eyes_frame = tk.Frame(root)
eyes_frame.pack(pady=10)

tk.Label(eyes_frame, text = "Eye Color:").grid(row = 0, column = 0)
tk.Button(eyes_frame, text="Blue", command=draw_eyes_blue, width=10).grid(row=0, column=0, padx=5)
tk.Button(eyes_frame, text="Light Brown", command=draw_eyes_hazel, width=10).grid(row=0, column=1, padx=5)
tk.Button(eyes_frame, text="Dark Brown", command=draw_eyes_brown, width=10).grid(row=0, column=2, padx=5)
tk.Button(eyes_frame, text="Green", command=draw_eyes_green, width=10).grid(row=0, column=3, padx=5)

eyebrow_frame = tk.Frame(root)
eyebrow_frame.pack(pady=10)

tk.Label(eyebrow_frame, text = "Eyebrows:").grid(row = 0, column = 0)
tk.Button(eyebrow_frame, text = "Raised", command = eyebrow_raised, width=10).grid(row=0, column=0, padx=5)
tk.Button(eyebrow_frame, text = "Neutral", command = eyebrow_neutral, width=10).grid(row=0, column=1, padx=5)
tk.Button(eyebrow_frame, text = "Angry", command = eyebrow_angry, width=10).grid(row=0, column=2, padx=5)

def draw_face_shade1():
    draw_face("#562a1d")

def draw_face_shade2():
    draw_face("#7a442a")

def draw_face_shade3():
    draw_face("#af7c4f")

def draw_face_shade4():
    draw_face("#e6c9ab")

def draw_face_shade5():
    draw_face("#efdccd")


tk.Button(face_frame, text="Shade 1", width=10, command=draw_face_shade1).grid(row=0, column=0)
tk.Button(face_frame, text="Shade 2", width=10, command=draw_face_shade2).grid(row=0, column=1)
tk.Button(face_frame, text="Shade 3", width=10, command=draw_face_shade3).grid(row=0, column=2)
tk.Button(face_frame, text="Shade 4", width=10, command=draw_face_shade4).grid(row=0, column=3)
tk.Button(face_frame, text="Shade 5", width=10, command=draw_face_shade5).grid(row=0, column=4)

win.exitonclick()
