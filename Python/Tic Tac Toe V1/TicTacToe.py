# Tic Tac Toe on Python programming language
import turtle
from GameFunction import *


# Function, that decides, what should to draw: cross or null
def choice(obj):
    global now
    if now == 1:
        drawFunc.cross(obj)
        now = 0
    elif now == 0:
        drawFunc.null(obj)
        now = 1


# Main game function
def game():
    global field1_flag, field2_flag, field3_flag, field4_flag, \
        field5_flag, field6_flag, field7_flag, field8_flag, field9_flag, now
    now = 1

    newGame.new_game(grid)

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


def click(x, y):
    global field1_flag, field2_flag, field3_flag, field4_flag, field5_flag, \
        field6_flag, field7_flag, field8_flag, field9_flag
    # field 1
    if -300 <= x <= -100 and 100 <= y <= 300 and field1_flag == 0:
        field1.clear()
        choice(field1)
        field1_flag = 1 if now == 0 else 2
    # field 2
    elif -100 <= x <= 100 <= y <= 300 and field2_flag == 0:  # -100 <= x <= 100 and 100 <= y <= 300
        field2.clear()
        choice(field2)
        field2_flag = 1 if now == 0 else 2
    # field 3
    elif 100 <= x <= 300 and 100 <= y <= 300 and field3_flag == 0:
        field3.clear()
        choice(field3)
        field3_flag = 1 if now == 0 else 2
    # field 4
    elif -300 <= x <= -100 <= y <= 100 and field4_flag == 0:  # -300 <= x <= -100 and -100 <= y <= 100
        field4.clear()
        choice(field4)
        field4_flag = 1 if now == 0 else 2
    # field 5
    elif -100 <= x <= 100 and -100 <= y <= 100 and field5_flag == 0:
        field5.clear()
        choice(field5)
        field5_flag = 1 if now == 0 else 2
    # field 6
    elif 300 >= x >= 100 >= y >= -100 and field6_flag == 0:  # 100 <= x <= 300 and -100 <= y <= 100
        field6.clear()
        choice(field6)
        field6_flag = 1 if now == 0 else 2
    # field 7
    elif -300 <= x <= -100 and -300 <= y <= -100 and field7_flag == 0:
        field7.clear()
        choice(field7)
        field7_flag = 1 if now == 0 else 2
    # field 8
    elif 100 >= x >= -100 >= y >= -300 and field8_flag == 0:  # -100 <= x <= 100 and -300 <= y <= -100
        field8.clear()
        choice(field8)
        field8_flag = 1 if now == 0 else 2
    # field 9
    elif 100 <= x <= 300 and -300 <= y <= -100 and field9_flag == 0:
        field9.clear()
        choice(field9)
        field9_flag = 1 if now == 0 else 2

    # List with parameters that determine whether the field is filled in or not
    fields = [field1_flag, field2_flag, field3_flag, field4_flag, field5_flag,
              field6_flag, field7_flag, field8_flag, field9_flag]

    # List with combinations to check win
    w1 = fields[0] * fields[1] * fields[2]
    w2 = fields[3] * fields[4] * fields[5]
    w3 = fields[6] * fields[7] * fields[8]
    w4 = fields[0] * fields[3] * fields[6]
    w5 = fields[1] * fields[4] * fields[7]
    w6 = fields[2] * fields[5] * fields[8]
    w7 = fields[0] * fields[4] * fields[8]
    w8 = fields[2] * fields[4] * fields[6]
    combinations = [w1, w2, w3, w4, w5, w6, w7, w8]

    # Check win combinations
    if winReq.win(fields, combinations, window, writer):
        game()


# Create window 600x600
window = turtle.Screen()
window.title("Крестики Нолики")
window.setup(600, 600)

# The object, that draw a game field (grid)
grid = turtle.Turtle()
grid.speed(0)

# Object, that write a text: "Red Win", "Blue Win" or "GG"
writer = turtle.Turtle()
writer.speed(0)
writer.hideturtle()
writer.penup()
writer.goto(-150, 0)

# Nine objects, that draw in every game field (one field = one object)
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

game()

turtle.done()
