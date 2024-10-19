# function, that draws main field for game in window 600x600
def new_game(obj):
    obj.clear()
    obj.setheading(0)
    obj.pensize(5)

    obj.penup()
    obj.goto(-300, 100)
    obj.pendown()
    obj.forward(600)

    obj.penup()
    obj.goto(-300, -100)
    obj.pendown()
    obj.forward(600)

    obj.right(90)

    obj.penup()
    obj.goto(-100, 300)
    obj.pendown()
    obj.forward(600)

    obj.penup()
    obj.goto(100, 300)
    obj.pendown()
    obj.forward(600)
