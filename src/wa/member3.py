import turtle
win = turtle.Screen()
turt = turtle.Turtle()



def draw_face(color):
        # move turtle to position to start drawing face
    turt.hideturtle()
    turt.speed(0)
    turt.penup()
    turt.right(90)
    turt.forward(150)
    turt.left(90)
    turt.pendown()
        # set turtle color to inputted color
    turt.pencolor(color)
    turt.fillcolor(color)
    turt.begin_fill()
        # draw face
    for x in range(2):
        turt.circle(120, 45)
        turt.circle(200, 90)
        turt.circle(120, 45)
    turt.end_fill()
        # go back to center
    turt.penup()
    turt.goto(0, 0)
    turt.pendown()


def draw_mouth(mouth_type, x, y,size):
    turt = turtle.Turtle()
    turt.speed(0)
    turt.penup()
    turt.goto(x, y)
    turt.pendown()
    turt.width(3)

    if mouth_type == 'smile':
        turt.setheading(270)
        turt.circle(size, 180)
    elif mouth_type == 'frown':
        turt.setheading(90)
        turt.circle(size, 180)
    elif mouth_type == 'excited':
        turt.setheading(0)
        turt.setheading(0)
        turt.circle(size)
    else:
        print("Invalid mouth_type. Choose 'smile', 'frown', or 'excited'.")

def background_fill():

def draw_glasses():

def draw_earrings():

draw_face('green')
draw_mouth('frown',    50,   -100, 50)
draw_mouth('smile',      -50,   -60, 50)
draw_mouth('excited', 0, -100, 40)



turtle.done()