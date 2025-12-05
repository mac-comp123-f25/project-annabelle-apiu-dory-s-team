import turtle
import tkinter as tk

# Tkinter Window + Turtle Setup
root = tk.Tk()
root.title("Mouth Drawer")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

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
    draw_mouth("smile", -48, -70, 50)

def draw_frown():
    draw_mouth("frown", 45, -100, 50)

def draw_excited():
    draw_mouth("excited", 0, -100, 40)

def draw_ears_only():
    draw_ears(False)

def draw_ears_with_earrings():
    draw_ears(True)
def draw_nose(t, size="medium"):
    t.penup()
    t.goto(-20, 45)
    t.setheading(-90)
    t.pendown()
    t.pensize(2)

    if size.lower() == "small":
        scale = 0.5
    elif size.lower() == "big":
        scale = 1.5
    else:
        scale = 1  # default/medium

    t.begin_fill()
    t.forward(12 * scale)
    t.right(10)
    t.circle(20 * scale, 40)   # outer curve
    t.circle(10 * scale, 80)   # inner curve

    t.setheading(0)
    t.circle(8 * scale, 70)    # bottom curve

    t.setheading(0)
    t.circle(15 * scale, 90)   # right nostril
    t.circle(10 * scale, 60)
    t.end_fill()

def draw_nose_from_input():
    size = nose_entry.get()
    nose_turtle.clear()  # remove previous nose
    draw_nose(nose_turtle, size)
    win.update()

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

def draw_hair_strands(t, color, start_x=145, start_y=146, strands=20):
    t.hideturtle()
    t.pencolor(color)
    t.pensize(3)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    for i in range(strands):
        t.setheading(130)
        t.circle(150, 60)
        t.circle(150, 60)
        t.penup()
        t.goto(start_x - (i * 3), start_y)
        t.pendown()

def draw_selected_hair():
    hair_color = color_entry.get() or "black"
    mode = hair_mode.get()
    hair_turtle.clear()
    hair_turtle.speed(0)

    if mode == "bun":
        draw_hair_bun(hair_turtle, hair_color)
    else:
        draw_hair_strands(hair_turtle, hair_color, start_x=145, start_y=146, strands=20)

    win.update()



# Create Buttons
mouth_frame = tk.Frame(root)
mouth_frame.pack(pady=10)

tk.Button(mouth_frame, text="Smile", command=draw_smile, width=10).grid(row=0, column=0, padx=5)
tk.Button(mouth_frame, text="Frown", command=draw_frown, width=10).grid(row=0, column=1, padx=5)
tk.Button(mouth_frame, text="Excited", command=draw_excited, width=10).grid(row=0, column=2, padx=5)

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


# Draw initial face
draw_face('green')

# Run the App
root.mainloop()
