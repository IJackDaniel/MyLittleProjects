# Tic Tac Toe on Python programming language
import turtle
from time import sleep


# function, that draws main field for game
def new_game():
    setka.clear()
    setka.setheading(0)
    setka.pensize(5)

    setka.penup()
    setka.goto(-300, 100)
    setka.pendown()
    setka.forward(600)

    setka.penup()
    setka.goto(-300, -100)
    setka.pendown()
    setka.forward(600)

    setka.right(90)

    setka.penup()
    setka.goto(-100, 300)
    setka.pendown()
    setka.forward(600)

    setka.penup()
    setka.goto(100, 300)
    setka.pendown()
    setka.forward(600)


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


# function, that decides, what should to draw: cross or null
def choice(obj):
    global now
    if now == 1:
        cross(obj)
        now = 0
    elif now == 0:
        null(obj)
        now = 1


def click(x, y):
    global field1_flag, field2_flag, field3_flag, field4_flag, field5_flag, \
        field6_flag, field7_flag, field8_flag, field9_flag
    # field 1
    if -300 <= x <= -100 and 100 <= y <= 300 and field1_flag == 0:
        field1.clear()
        choice(field1)
        field1_flag = 1 if now == 0 else 2
    # field 2
    elif -100 <= x <= 100 and 100 <= y <= 300 and field2_flag == 0:
        field2.clear()
        choice(field2)
        field2_flag = 1 if now == 0 else 2
    # field 3
    elif 100 <= x <= 300 and 100 <= y <= 300 and field3_flag == 0:
        field3.clear()
        choice(field3)
        field3_flag = 1 if now == 0 else 2
    # field 4
    elif -300 <= x <= -100 and -100 <= y <= 100 and field4_flag == 0:
        field4.clear()
        choice(field4)
        field4_flag = 1 if now == 0 else 2
    # field 5
    elif -100 <= x <= 100 and -100 <= y <= 100 and field5_flag == 0:
        field5.clear()
        choice(field5)
        field5_flag = 1 if now == 0 else 2
    # field 6
    elif 100 <= x <= 300 and -100 <= y <= 100 and field6_flag == 0:
        field6.clear()
        choice(field6)
        field6_flag = 1 if now == 0 else 2
    # field 7
    elif -300 <= x <= -100 and -300 <= y <= -100 and field7_flag == 0:
        field7.clear()
        choice(field7)
        field7_flag = 1 if now == 0 else 2
    # field 8
    elif -100 <= x <= 100 and -300 <= y <= -100 and field8_flag == 0:
        field8.clear()
        choice(field8)
        field8_flag = 1 if now == 0 else 2
    # field 9
    elif 100 <= x <= 300 and -300 <= y <= -100 and field9_flag == 0:
        field9.clear()
        choice(field9)
        field9_flag = 1 if now == 0 else 2

    arr = [field1_flag, field2_flag, field3_flag, field4_flag, field5_flag,
           field6_flag, field7_flag, field8_flag, field9_flag]

    # win combinations
    w1 = arr[0]*arr[1]*arr[2]
    w2 = arr[3]*arr[4]*arr[5]
    w3 = arr[6]*arr[7]*arr[8]
    w4 = arr[0]*arr[3]*arr[6]
    w5 = arr[1]*arr[4]*arr[7]
    w6 = arr[2]*arr[5]*arr[8]
    w7 = arr[0]*arr[4]*arr[8]
    w8 = arr[2]*arr[4]*arr[6]
    """"запиши каждую из переменных w1-w8 как СЛОВАРЬ со значениями из полей.
    Создаю функцию, которая будет принимать словарь, а возвращать произведение его значений по ключам. Это нужно
    для проверки условия выигрыша. Потом со словаря можно достать номера полей, которые составляют "тройку".
    """
    # Win Player 1
    if ((w1 == 1) or (w2 == 1) or (w3 == 1) or (w4 == 1) or (w5 == 1) or (w6 == 1) or
            (w7 == 1) or (w8 == 1)):
        window.clear()



        sleep(10)
        writer.clear()
        game()
    # Win Player 2
    elif ((w1 == 8) or (w2 == 8) or (w3 == 8) or (w4 == 8) or (w5 == 8) or (w6 == 8) or
            (w7 == 8) or (w8 == 8)):
        window.clear()
        # writer.write("Blue Win!", font=("Arial", 50, "bold"))
        sleep(10)
        writer.clear()
        game()
    # Draw
    elif 0 not in arr:
        window.clear()
        a = 100
        writer.forward(a)
        # writer.write("GG", font=("Arial", 50, "bold"))
        writer.backward(a)
        sleep(10)
        writer.clear()
        game()


# create window
window = turtle.Screen()
window.title("Крестики Нолики")
window.setup(600, 600)

setka = turtle.Turtle()
setka.speed(0)

writer = turtle.Turtle()
writer.speed(0)
writer.hideturtle()

winLine = turtle.Turtle()
winLine.hideturtle()
winLine.speed(0)
winLine.pensize(5)
winLine.penup()

field1 = turtle.Turtle()
field2 = turtle.Turtle()
field3 = turtle.Turtle()
field4 = turtle.Turtle()
field5 = turtle.Turtle()
field6 = turtle.Turtle()
field7 = turtle.Turtle()
field8 = turtle.Turtle()
field9 = turtle.Turtle()

field1.hideturtle()
field2.hideturtle()
field3.hideturtle()
field4.hideturtle()
field5.hideturtle()
field6.hideturtle()
field7.hideturtle()
field8.hideturtle()
field9.hideturtle()

field1.speed(0)
field2.speed(0)
field3.speed(0)
field4.speed(0)
field5.speed(0)
field6.speed(0)
field7.speed(0)
field8.speed(0)
field9.speed(0)

field1.pensize(5)
field2.pensize(5)
field3.pensize(5)
field4.pensize(5)
field5.pensize(5)
field6.pensize(5)
field7.pensize(5)
field8.pensize(5)
field9.pensize(5)

field1.penup()
field1.goto(-300, 300)
field2.penup()
field2.goto(-100, 300)
field3.penup()
field3.goto(100, 300)
field4.penup()
field4.goto(-300, 100)
field5.penup()
field5.goto(-100, 100)
field6.penup()
field6.goto(100, 100)
field7.penup()
field7.goto(-300, -100)
field8.penup()
field8.goto(-100, -100)
field9.penup()
field9.goto(100, -100)


def game():
    global field1_flag, field2_flag, field3_flag, field4_flag, \
        field5_flag, field6_flag, field7_flag, field8_flag, field9_flag, now
    now = 1

    writer.penup()
    writer.goto(-150, 0)

    new_game()

    field1_flag = 0
    field2_flag = 0
    field3_flag = 0
    field4_flag = 0
    field5_flag = 0
    field6_flag = 0
    field7_flag = 0
    field8_flag = 0
    field9_flag = 0

    window.listen()

    window.onscreenclick(click, 1)


game()

turtle.done()
