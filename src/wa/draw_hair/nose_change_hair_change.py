import turtle
import tkinter as tk
def draw_face(color):
    turt.hideturtle()
    turt.penup()
    turt.right(90)
    turt.forward(150)
    turt.left(90)
    turt.pendown()
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
    for _ in range(2):
        turt.circle(120, 45)
        turt.circle(200, 90)
        turt.circle(120, 45)
    turt.end_fill()
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

#Tkinter window
root = tk.Tk()
root.title("Hair & Nose Drawer")

# Canvas for turtle
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

# Bottom controls frame
bottom_controls = tk.Frame(root)
bottom_controls.pack(side="bottom", pady=10)

# Hair color
tk.Label(bottom_controls, text="Hair color:").pack(side="left", padx=5)
color_entry = tk.Entry(bottom_controls, width=10)
color_entry.pack(side="left", padx=5)
color_entry.insert(0, "black")

# Hair mode radio buttons
hair_mode = tk.StringVar(value="bun")
tk.Radiobutton(bottom_controls, text="Bun", variable=hair_mode, value="bun").pack(side="left", padx=5)
tk.Radiobutton(bottom_controls, text="Strands", variable=hair_mode, value="strands").pack(side="left", padx=5)

# Draw Hair button
tk.Button(bottom_controls, text="Draw Hair", command=draw_selected_hair).pack(side="left", padx=5)

# Nose size
tk.Label(bottom_controls, text="Nose size:").pack(side="left", padx=5)
nose_entry = tk.Entry(bottom_controls, width=8)
nose_entry.pack(side="left", padx=5)

# Draw Nose button
tk.Button(bottom_controls, text="Draw Nose", command=draw_nose_from_input).pack(side="left", padx=5)

#Turtle setup
win = turtle.TurtleScreen(canvas)#connects the turtles to the canvas
win.tracer(0, 0)  # speedy drawing

turt = turtle.RawTurtle(canvas)
turt.speed(0)
draw_face("brown")

hair_turtle = turtle.RawTurtle(canvas)
hair_turtle.speed(0)

nose_turtle = turtle.RawTurtle(canvas)
nose_turtle.hideturtle()
nose_turtle.speed(0)

# Default hair and nose
draw_hair_bun(hair_turtle, "black")
draw_nose(nose_turtle)
win.update()

root.mainloop()
