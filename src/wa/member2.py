import turtle


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
        #turt.end_fill()


def draw_nose(t):
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.pensize(2)


    t.begin_fill()
    t.forward(12)
    t.right(10)
    t.circle(20, 40)   # small outer curve
    t.circle(10, 80)   # small inner curve

    t.setheading(0)
    t.circle(8, 70)    # bottom curve

    t.setheading(0)
    t.circle(15, 90)   # right nostril
    t.circle(10, 60)
    t.end_fill()


def draw_hair_strands(t, color, start_x, start_y, strands=10, length=120):
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
        t.goto(start_x - (i * 2), start_y)
        t.pendown()


win = turtle.Screen()
turt = turtle.Turtle()
turt.speed(5)

draw_face("brown")
left_turtle=turtle.Turtle()
left_turtle.speed(20)
draw_hair_strands(left_turtle,"black",145,146,strands=25,length=250)

nose_turtle = turtle.Turtle()
nose_turtle.hideturtle()
nose_turtle.speed(5)
draw_nose(nose_turtle)

win.exitonclick()
