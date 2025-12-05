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

def draw_hair_bun(t, color):
    t.hideturtle()
    t.penup()
    t.goto(0, 190)    # Top of the head
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(60)      # Bun shape
    t.end_fill()

    # small base to connect bun to head
    t.penup()
    t.goto(-40, 200)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(80)
        t.right(90)
        t.forward(20)
        t.right(90)
    t.end_fill()

def draw_hair_from_input():
    hair_color = color_entry.get()
    hair_turtle.clear()
    hair_turtle.speed(0)
    draw_hair_bun(hair_turtle, hair_color)
    win.update()

# tkinter window
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
root.title("Hair Color")

tk.Label(root, text="Enter hair color:").pack(pady=5)
color_entry = tk.Entry(root)
color_entry.pack(pady=5)
tk.Button(root, text="Draw Hair", command=draw_hair_from_input).pack(pady=10)

win = turtle.TurtleScreen(canvas)
win.tracer(0, 0)

turt = turtle.RawTurtle(canvas)
turt.speed(0)

draw_face("brown")

hair_turtle = turtle.RawTurtle(canvas)
hair_turtle.speed(0)
draw_hair_bun(hair_turtle, "black")  # Default bun
win.update()

nose_turtle = turtle.RawTurtle(canvas)
nose_turtle.hideturtle()
nose_turtle.speed(0)
draw_nose(nose_turtle)

root.mainloop()
