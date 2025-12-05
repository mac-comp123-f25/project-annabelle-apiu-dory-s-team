import turtle
import tkinter as tk

# Global layout parameters
HEAD_CENTER_X = 0
HEAD_CENTER_Y = 50
HEAD_RADIUS = 120


def draw_face(color):
    turt.hideturtle()
    turt.penup()
    turt.goto(HEAD_CENTER_X, HEAD_CENTER_Y - HEAD_RADIUS)
    turt.setheading(0)
    turt.pendown()
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(HEAD_RADIUS)
    turt.end_fill()

# ---------------- NOSE ----------------
def draw_nose(t, size="medium"):
    nose_x = HEAD_CENTER_X
    nose_y = HEAD_CENTER_Y - 20
    t.penup()
    t.goto(nose_x, nose_y)
    t.setheading(-90)
    t.pendown()
    t.pensize(2)

    if size.lower() == "small":
        scale = 0.5
    elif size.lower() == "big":
        scale = 1.5
    else:
        scale = 1

    t.begin_fill()
    t.forward(12 * scale)
    t.right(10)
    t.circle(20 * scale, 40)
    t.circle(10 * scale, 80)
    t.setheading(0)
    t.circle(8 * scale, 70)
    t.setheading(0)
    t.circle(15 * scale, 90)
    t.circle(10 * scale, 60)
    t.end_fill()

def draw_nose_from_input():
    size = nose_entry.get()
    nose_turtle.clear()
    draw_nose(nose_turtle, size)
    win.update()

# ---------------- BUN HAIR ----------------
def draw_hair_bun(t, color):
    bun_x = HEAD_CENTER_X
    bun_y = HEAD_CENTER_Y + HEAD_RADIUS + 40
    t.hideturtle()
    t.penup()
    t.goto(bun_x, bun_y)
    t.setheading(0)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)

    # Bun
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    # Connector under bun
    t.penup()
    t.goto(bun_x - 35, bun_y - 10)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(70)
        t.right(90)
        t.forward(18)
        t.right(90)
    t.end_fill()


def draw_shoulder_hair(t, color):
    t.hideturtle()
    t.pencolor(color)
    t.fillcolor(color)


    left_start_x = HEAD_CENTER_X - 90
    left_start_y = HEAD_CENTER_Y + 130
    t.penup()
    t.goto(left_start_x, left_start_y)
    t.setheading(100)
    t.pendown()
    t.begin_fill()
    t.circle(120, 90)
    t.circle(40, 60)
    t.goto(HEAD_CENTER_X - 50, HEAD_CENTER_Y - 20)
    t.goto(left_start_x, left_start_y)
    t.end_fill()

    right_start_x = HEAD_CENTER_X + 90
    right_start_y = HEAD_CENTER_Y + 150
    t.penup()
    t.goto(right_start_x, right_start_y)
    t.setheading(-30)
    t.pendown()
    t.begin_fill()
    t.circle(-120, 90)
    t.circle(-40, 60)
    t.goto(HEAD_CENTER_X + 50, HEAD_CENTER_Y - 20)
    t.goto(right_start_x, right_start_y)
    t.end_fill()

    # --- TOP CAP ---
    t.penup()
    t.goto(HEAD_CENTER_X +75, HEAD_CENTER_Y + 120)
    t.setheading(90)
    t.pendown()
    t.begin_fill()
    t.circle(60, 180)
    t.goto(HEAD_CENTER_X - 60, HEAD_CENTER_Y + 120)
    t.end_fill()


def draw_selected_hair():
    hair_color = color_entry.get() or "black"
    style = hair_mode.get()
    hair_turtle.clear()
    hair_turtle.speed(0)

    if style == "bun":
        draw_hair_bun(hair_turtle, hair_color)
    elif style == "shoulder":
        draw_shoulder_hair(hair_turtle, hair_color)

    win.update()


root = tk.Tk()
root.title("Hair & Nose Drawer (Aligned)")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

bottom_controls = tk.Frame(root)
bottom_controls.pack(side="bottom", pady=10)

# Hair color input
tk.Label(bottom_controls, text="Hair color:").pack(side="left", padx=5)
color_entry = tk.Entry(bottom_controls, width=12)
color_entry.pack(side="left", padx=5)
color_entry.insert(0, "black")

# Hair style
hair_mode = tk.StringVar(value="shoulder")
tk.Radiobutton(bottom_controls, text="Bun", value="bun", variable=hair_mode).pack(side="left", padx=5)
tk.Radiobutton(bottom_controls, text="Shoulder Length", value="shoulder", variable=hair_mode).pack(side="left", padx=5)

tk.Button(bottom_controls, text="Draw Hair", command=draw_selected_hair).pack(side="left", padx=8)

# Nose input
tk.Label(bottom_controls, text="Nose size:").pack(side="left", padx=5)
nose_entry = tk.Entry(bottom_controls, width=8)
nose_entry.pack(side="left", padx=5)
tk.Button(bottom_controls, text="Draw Nose", command=draw_nose_from_input).pack(side="left", padx=5)


win = turtle.TurtleScreen(canvas)
win.tracer(0, 0)

turt = turtle.RawTurtle(canvas)
turt.hideturtle()
turt.speed(0)

hair_turtle = turtle.RawTurtle(canvas)
hair_turtle.hideturtle()
hair_turtle.speed(0)

nose_turtle = turtle.RawTurtle(canvas)
nose_turtle.hideturtle()
nose_turtle.speed(0)

# Draw initial face, shoulder hair, and nose
draw_face("brown")
draw_shoulder_hair(hair_turtle, "black")
draw_nose(nose_turtle)
win.update()

root.mainloop()
