import turtle
import tkinter as tk

# Tkinter Window + Turtle Setup
root = tk.Tk()
root.title("Avatar Maker")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack(side = "right")

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("white")

face_turt = turtle.RawTurtle(screen)   # For face
face_turt.hideturtle()
face_turt.speed(0)

mouth_turt = turtle.RawTurtle(screen)  # For mouths
mouth_turt.hideturtle()
mouth_turt.speed(0)
mouth_turt.width(3)

bg_turt = turtle.RawTurtle(screen)     # For background
bg_turt.hideturtle()
bg_turt.speed(0)

ear_turt = turtle.RawTurtle(screen)    #For ears
ear_turt.hideturtle()
ear_turt.speed(0)

#hair and the nose turtle
hair_turtle=turtle.RawTurtle(screen)
hair_turtle.hideturtle()
hair_turtle.speed(0)
nose_turtle = turtle.RawTurtle(screen)
nose_turtle.hideturtle()
nose_turtle.speed(0)

eyes_turt = turtle.RawTurtle(screen)
eyes_turt.speed(0)
eyes_turt.hideturtle()

eyebrow_turt = turtle.RawTurtle(screen)
eyebrow_turt.color("black")
eyebrow_turt.width(8)
eyebrow_turt.speed(0)
eyebrow_turt.hideturtle()

hair_turtle=turtle.RawTurtle(screen)
hair_turtle.hideturtle()
hair_turtle.speed(0)
right_hair=turtle.RawTurtle(screen)
right_hair.hideturtle()
right_hair.speed(0)
center_hair=turtle.RawTurtle(screen)
center_hair.hideturtle()
center_hair.speed(0)

# Face Drawing
def draw_face(color):
    face_turt.penup()
    face_turt.goto(0, 0)
    face_turt.setheading(0)
    face_turt.right(90)
    face_turt.forward(150)
    face_turt.left(90)
    face_turt.pendown()
    face_turt.pencolor(color)
    face_turt.fillcolor(color)
    face_turt.begin_fill()
    for x in range(2):
        face_turt.circle(120, 45)
        face_turt.circle(200, 90)
        face_turt.circle(120, 45)
    face_turt.end_fill()
    face_turt.penup()
    face_turt.goto(0, 0)
    face_turt.pendown()

# Mouth Drawing
def draw_mouth(mouth_type, x, y, size):
    mouth_turt.clear()
    mouth_turt.penup()
    mouth_turt.goto(x, y)
    mouth_turt.pendown()

    if mouth_type == 'smile':
        mouth_turt.setheading(270)
        mouth_turt.circle(size, 180)
    elif mouth_type == 'frown':
        mouth_turt.setheading(90)
        mouth_turt.circle(size, 180)
    elif mouth_type == 'excited':
        mouth_turt.setheading(0)
        mouth_turt.circle(size)

#Ear functions
def draw_ears(include_earrings=False):
    ear_color = face_turt.fillcolor()

    ear_turt.clear()
    ear_turt.penup()
    ear_turt.pencolor("black")
    ear_turt.fillcolor(ear_color)

    # LEFT EAR
    ear_turt.goto(-142, 40)
    ear_turt.setheading(90)
    ear_turt.begin_fill()
    ear_turt.pendown()
    ear_turt.circle(35, 110)
    ear_turt.circle(20, 130)
    ear_turt.circle(35, 110)
    ear_turt.end_fill()
    ear_turt.penup()

    if include_earrings:
        ear_turt.fillcolor("gold")
        ear_turt.pencolor("gold")
        ear_turt.goto(-165, 29)
        ear_turt.begin_fill()
        ear_turt.circle(8)
        ear_turt.end_fill()

    # RIGHT EAR
    ear_turt.pencolor("black")
    ear_turt.fillcolor(ear_color)

    ear_turt.goto(142, 40)
    ear_turt.setheading(90)
    ear_turt.begin_fill()
    ear_turt.pendown()

    ear_turt.circle(-35, 110)
    ear_turt.circle(-20, 130)
    ear_turt.circle(-35, 110)
    ear_turt.end_fill()
    ear_turt.penup()

    if include_earrings:
        ear_turt.fillcolor("gold")
        ear_turt.pencolor("gold")
        ear_turt.goto(176, 35)
        ear_turt.begin_fill()
        ear_turt.circle(8)
        ear_turt.end_fill()

# Background Functions
def bg_solid(color):
    screen.bgcolor(color)

# Button Functions
def draw_smile():
    draw_mouth("smile", -48, -50, 50)

def draw_frown():
    draw_mouth("frown", 45, -100, 50)

def draw_excited():
    draw_mouth("excited", 0, -100, 40)

def draw_ears_only():
    draw_ears(False)

def draw_ears_with_earrings():
    draw_ears(True)

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


def draw_nose_small():
    nose_turtle.clear()
    nose_turtle.penup()
    nose_turtle.goto(-20, 40)
    nose_turtle.setheading(-90)
    nose_turtle.pendown()
    nose_turtle.pensize(2)

    nose_turtle.begin_fill()
    nose_turtle.forward(6)
    nose_turtle.right(10)
    nose_turtle.circle(5, 30)   # outer curve
    nose_turtle.circle(3, 70)   # inner curve

    nose_turtle.setheading(0)
    nose_turtle.circle(4, 70)   # bottom curve

    nose_turtle.setheading(0)
    nose_turtle.circle(7, 90)   # right nostril
    nose_turtle.circle(5, 60)
    nose_turtle.end_fill()




def draw_nose_medium():
    nose_turtle.clear()
    nose_turtle.penup()
    nose_turtle.goto(-20, 40)
    nose_turtle.setheading(-90)
    nose_turtle.pendown()
    nose_turtle.pensize(2)

    nose_turtle.begin_fill()
    nose_turtle.forward(12)
    nose_turtle.right(10)
    nose_turtle.circle(10, 30)   # outer curve
    nose_turtle.circle(5, 70)    # inner curve

    nose_turtle.setheading(0)
    nose_turtle.circle(8, 70)    # bottom curve

    nose_turtle.setheading(0)
    nose_turtle.circle(15, 90)   # right nostril
    nose_turtle.circle(10, 60)
    nose_turtle.end_fill()




def draw_nose_big():
    nose_turtle.clear()
    nose_turtle.penup()
    nose_turtle.goto(-20, 40)
    nose_turtle.setheading(-90)
    nose_turtle.pendown()
    nose_turtle.pensize(2)

    nose_turtle.begin_fill()
    nose_turtle.forward(18)
    nose_turtle.right(10)
    nose_turtle.circle(15, 30)   # outer curve
    nose_turtle.circle(10, 70)   # inner curve

    nose_turtle.setheading(0)
    nose_turtle.circle(12, 70)   # bottom curve

    nose_turtle.setheading(0)
    nose_turtle.circle(20, 90)   # right nostril
    nose_turtle.circle(15, 60)
    nose_turtle.end_fill()






def draw_hair_bun(t, color):
    t.hideturtle()
    t.penup()
    t.goto(0, 190)  # Top of the head
    t.setheading(0)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)

    # Draw bun circle
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    # Draw connector rectangle
    t.penup()
    t.goto(-40, 200)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(80)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()

def draw_hair():
    hair_turtle.pensize(30)
    hair_turtle.hideturtle()
    hair_turtle.penup()
    hair_turtle.goto(65,200)
    hair_turtle.pendown()
    hair_turtle.setheading(310)
    hair_turtle.begin_fill()
    hair_turtle.circle(-410,23)
    #hair_turtle.forward(50)
    hair_turtle.end_fill()

    # left hair
    right_hair.penup()
    right_hair.pensize(30)
    right_hair.hideturtle()
    right_hair.goto(-50,194)
    right_hair.pendown()
    right_hair.begin_fill()
    right_hair.setheading(220)
    right_hair.circle(410,22)
    right_hair.end_fill()
    #center piece
    center_hair.pensize(30)
    center_hair.penup()
    center_hair.hideturtle()
    center_hair.goto(-70, 195)  
    center_hair.pendown()
    center_hair.begin_fill()
    center_hair.setheading(5)
    center_hair.circle(-420, 20)
    center_hair.end_fill()
    screen.update()

def draw_selected_hair():
    hair_color ="black"
    mode = hair_mode.get()
    hair_turtle.clear()
    hair_turtle.speed(0)

    if mode == "bun":
        draw_hair_bun(hair_turtle, hair_color)
    else:
        draw_hair()
    screen.update()

def draw_eyes(color):
    eyes_turt.clear()
    eyes_turt.penup()
    eyes_turt.setheading(0)
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
    screen.update()

def draw_eyes_blue():
    draw_eyes("light blue")

def draw_eyes_green():
    draw_eyes("#92b092")

def draw_eyes_brown():
    draw_eyes("#73491c")

def draw_eyes_hazel():
    draw_eyes("#967b51")

def eyebrow_raised():
    eyebrow_turt.clear()
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
    eyebrow_turt.clear()
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
    eyebrow_turt.clear()
    eyebrow_turt.penup()
    eyebrow_turt.goto(110, 115)
    eyebrow_turt.setheading(180)
    eyebrow_turt.pendown()
    eyebrow_turt.forward(70)
    eyebrow_turt.penup()
    eyebrow_turt.forward(70)
    eyebrow_turt.pendown()
    eyebrow_turt.forward(70)

def clear_all():
    face_turt.clear()
    mouth_turt.clear()
    bg_turt.clear()
    ear_turt.clear()
    hair_turtle.clear()
    nose_turtle.clear()
    eyes_turt.clear()
    center_hair.clear()
    right_hair.clear()
    eyebrow_turt.clear()
    screen.bgcolor("white")
    screen.update()


face_frame = tk.Frame(root)
face_frame.pack(pady = 10)

tk.Label(face_frame, text="Skin Color:").grid(row=0, column=0)
tk.Button(face_frame, text="Shade 1", width=5, command=draw_face_shade1).grid(row=0, column=1)
tk.Button(face_frame, text="Shade 2", width=5, command=draw_face_shade2).grid(row=0, column=2)
tk.Button(face_frame, text="Shade 3", width=5, command=draw_face_shade3).grid(row=0, column=3)
tk.Button(face_frame, text="Shade 4", width=5, command=draw_face_shade4).grid(row=0, column=4)
tk.Button(face_frame, text="Shade 5", width=5, command=draw_face_shade5).grid(row=0, column=5)

# Create Buttons
mouth_frame = tk.Frame(root)
mouth_frame.pack(pady=10)

tk.Label(mouth_frame, text="Mouth:").grid(row=0, column=0)
tk.Button(mouth_frame, text="Smile", command=draw_smile, width=10).grid(row=0, column=1, padx=5)
tk.Button(mouth_frame, text="Frown", command=draw_frown, width=10).grid(row=0, column=2, padx=5)
tk.Button(mouth_frame, text="Excited", command=draw_excited, width=10).grid(row=0, column=3, padx=5)

bg_frame = tk.Frame(root)
bg_frame.pack(pady=10)

tk.Label(bg_frame, text="Backgrounds:").grid(row=0, column=0)
tk.Button(bg_frame, text="Blue", width=10, command=lambda: bg_solid("lightblue")).grid(row=0, column=1)
tk.Button(bg_frame, text="Pink", width=10, command=lambda: bg_solid("pink")).grid(row=0, column=2)
tk.Button(bg_frame, text="Yellow", width=10, command=lambda: bg_solid("yellow")).grid(row=0, column=3)
tk.Button(bg_frame, text="Orange", width=10, command=lambda: bg_solid("orange")).grid(row=0, column=4)

ears_frame = tk.Frame(root)
ears_frame.pack(pady=10)

tk.Label(ears_frame, text="Ears:").grid(row=0, column=0)
tk.Button(ears_frame, text="Ears Only", width=12, command=draw_ears_only).grid(row=0, column=1)
tk.Button(ears_frame, text="Ears + Earrings", width=12, command=draw_ears_with_earrings).grid(row=0, column=2)

#frames for the nose and other entries
bottom_controls = tk.Frame(root)
bottom_controls.pack(pady=10)



# Draw Hair button
tk.Button(bottom_controls, text="Draw Hair", command=draw_selected_hair).pack(side="left", padx=5)
#hair mode and buttons
hair_mode = tk.StringVar(value="bun")
tk.Radiobutton(bottom_controls, text="Bun", variable=hair_mode, value="bun").pack(side="left", padx=5)
tk.Radiobutton(bottom_controls, text="Strands", variable=hair_mode, value="strands").pack(side="left", padx=5)

# Draw Nose button
#tk.Button(bottom_controls, text="Draw Nose", command=draw_nose_from_input).pack(side="left", padx=5)

nose_frame = tk.Frame(root)
nose_frame.pack(pady=20)
tk.Label(nose_frame, text="nose size:").grid(row=0, column=0)
tk.Button(nose_frame, text="Small", command=draw_nose_small, width=10).grid(row=0, column=1, padx=5)
tk.Button(nose_frame, text="medium", command=draw_nose_medium, width=10).grid(row=0, column=2, padx=5)
tk.Button(nose_frame, text="big", command=draw_nose_big, width=10).grid(row=0, column=3, padx=5)

eyes_frame = tk.Frame(root)
eyes_frame.pack(pady=10)

tk.Label(eyes_frame, text = "Eye Color:").grid(row = 0, column = 0)
tk.Button(eyes_frame, text="Blue", command=draw_eyes_blue, width=10).grid(row=0, column=1, padx=5)
tk.Button(eyes_frame, text="Light Brown", command=draw_eyes_hazel, width=10).grid(row=0, column=2, padx=5)
tk.Button(eyes_frame, text="Dark Brown", command=draw_eyes_brown, width=10).grid(row=0, column=3, padx=5)
tk.Button(eyes_frame, text="Green", command=draw_eyes_green, width=10).grid(row=0, column=4, padx=5)

eyebrow_frame = tk.Frame(root)
eyebrow_frame.pack(pady=10)

tk.Label(eyebrow_frame, text = "Eyebrows:").grid(row = 0, column = 0)
tk.Button(eyebrow_frame, text = "Raised", command = eyebrow_raised, width=10).grid(row=0, column=1, padx=5)
tk.Button(eyebrow_frame, text = "Neutral", command = eyebrow_neutral, width=10).grid(row=0, column=2, padx=5)
tk.Button(eyebrow_frame, text = "Angry", command = eyebrow_angry, width=10).grid(row=0, column=3, padx=5)

clear_frame = tk.Frame(root)
clear_frame.pack(pady=10)
tk.Button(clear_frame, text="Clear All", width=15, fg="black", command=clear_all).pack()

screen.tracer()
screen.update()

# Run the App
root.mainloop()

