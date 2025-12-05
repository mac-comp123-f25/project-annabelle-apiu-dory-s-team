import turtle
import tkinter as tk

# ---------- Drawing primitives (face, nose) ----------
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

def draw_nose(t):
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.pensize(2)

    t.begin_fill()
    t.forward(12)
    t.right(10)
    t.circle(20, 40)
    t.circle(10, 80)

    t.setheading(0)
    t.circle(8, 70)

    t.setheading(0)
    t.circle(15, 90)
    t.circle(10, 60)
    t.end_fill()

# ---------- Bun drawing (connector hidden inside bun) ----------
def draw_hair_bun(t, color):
    t.hideturtle()
    t.penup()
    t.goto(0, 190)  # Top of the head
    t.setheading(0)  # reset heading to default
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)

    # Draw bun circle
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    # Draw connector
    t.penup()
    t.goto(-40, 200)
    t.setheading(0)  # reset to ensure rectangle is aligned
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(80)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()



def draw_hair_strands(t, color, start_x=145, start_y=146, strands=25):
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
        t.goto(start_x - (i * 3), start_y)  # slight horizontal offset for layering
        t.pendown()


def draw_selected_hair():
    hair_color = color_entry.get() or "black"
    mode = hair_mode.get()

    hair_turtle.clear()
    hair_turtle.speed(0)

    if mode == "bun":
        draw_hair_bun(hair_turtle, hair_color)
    else:
        # strands
        draw_hair_strands(hair_turtle, hair_color, start_x=145, start_y=146, strands=25)

    win.update()

# ---------- Tkinter + Turtle setup ----------
root = tk.Tk()
root.title("Hair: Bun (default) or Strands")

# Canvas for turtle
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

# Controls
controls = tk.Frame(root)
controls.pack(pady=6)

tk.Label(controls, text="Enter hair color:").grid(row=0, column=0, padx=6)
color_entry = tk.Entry(controls)
color_entry.grid(row=0, column=1, padx=6)
color_entry.insert(0, "black")  # sensible default

# Radio buttons for mode selection (default = bun)
hair_mode = tk.StringVar(value="bun")
tk.Radiobutton(controls, text="Bun (default)", variable=hair_mode, value="bun").grid(row=1, column=0, sticky="w", padx=6)
tk.Radiobutton(controls, text="Strands", variable=hair_mode, value="strands").grid(row=1, column=1, sticky="w", padx=6)

tk.Button(controls, text="Draw Hair", command=draw_selected_hair).grid(row=2, column=0, columnspan=2, pady=8)

# Turtle screen
win = turtle.TurtleScreen(canvas)
win.tracer(0, 0)

# Main drawing turtles
turt = turtle.RawTurtle(canvas)       # for face
turt.speed(0)
hair_turtle = turtle.RawTurtle(canvas) # for hair (cleared/redrawn)
hair_turtle.speed(0)
nose_turtle = turtle.RawTurtle(canvas) # for nose
nose_turtle.hideturtle()
nose_turtle.speed(0)


draw_face("brown")
draw_nose(nose_turtle)
draw_hair_bun(hair_turtle, "black")
win.update()


root.mainloop()
