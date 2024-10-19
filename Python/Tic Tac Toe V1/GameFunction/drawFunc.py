# function, that draws cross
def cross(obj):
    coor = obj.pos()

    ln = int(200*(2**0.5) - 20*(2**0.5))

    obj.pencolor("red")
    obj.penup()
    obj.forward(10)
    obj.right(90)
    obj.forward(10)
    obj.left(45)

    obj.pendown()
    obj.forward(ln)
    obj.penup()
    obj.backward(int(ln/2))
    obj.right(90)
    obj.backward(int(ln/2))
    obj.pendown()
    obj.forward(ln)

    obj.setheading(0)
    obj.penup()
    obj.goto(coor)


# function, that draws null
def null(obj):
    obj.pencolor("Blue")
    coor = obj.pos()

    r = 85

    obj.penup()
    obj.forward(100)
    obj.right(90)
    obj.forward(180)
    obj.left(90)

    obj.pendown()
    obj.circle(r)
    obj.penup()

    obj.goto(coor)
