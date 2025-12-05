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

#hair and the nose turtle
hair_turtle=turtle.RawTurtle(screen)
hair_turtle.speed(0)
nose_turtle = turtle.RawTurtle(screen)
nose_turtle.hideturtle()
nose_turtle.speed(0)

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

    screen.update()
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

def draw_face_1():
    draw_face("brown")

def draw_face_2():
    draw_face("pink")


def draw_nose_small():
    nose_turtle.clear()
    nose_turtle.penup()
    nose_turtle.goto(-20, 45)
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
    nose_turtle.goto(-20, 45)
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
    nose_turtle.goto(-20, 45)
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

    screen.update()



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

face_frame = tk.Frame(root)
face_frame.pack(pady = 10)

tk.Label(bg_frame, text="Skin Color:").grid(row=2, column=0)
tk.Button(bg_frame, text="Color 1", width=10, command=draw_face_1).grid(row=2, column=1)
tk.Button(bg_frame, text="Color 2", width=10, command=draw_face_2).grid(row=2, column=2)

#frames for the nose and other entries
bottom_controls = tk.Frame(root)
bottom_controls.pack( pady=10)

# Hair color
tk.Label(bottom_controls, text="Hair color:").pack(side="left", padx=5)
color_entry = tk.Entry(bottom_controls, width=10)
color_entry.pack(side="left", padx=5)
color_entry.insert(0, "black")

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
tk.Button(nose_frame, text="Small", command=draw_nose_small, width=10).grid(row=0, column=0, padx=5)
tk.Button(nose_frame, text="medium", command=draw_nose_medium, width=10).grid(row=0, column=1, padx=5)
tk.Button(nose_frame, text="big", command=draw_nose_big, width=10).grid(row=0, column=2, padx=5)


#calling the nose and hair function
#draw_hair_strands(hair_turtle,"black", 145, 146, strands=25)#draws the default hair
screen.tracer(0,0)
screen.update()
#draw_nose(nose_turtle)


# Run the App
root.mainloop()

