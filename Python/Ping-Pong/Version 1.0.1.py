import pygame
from random import randint


def up_left():
    global x, y, dot_speed
    x -= dot_speed
    y -= dot_speed


def up_right():
    global x, y, dot_speed
    x += dot_speed
    y -= dot_speed


def down_left():
    global x, y, dot_speed
    x -= dot_speed
    y += dot_speed


def down_right():
    global x, y, dot_speed
    x += dot_speed
    y += dot_speed


table_height = 100
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600 + table_height))
done = False
y1 = 30 + table_height
x1 = 730
y2 = 30 + table_height
x2 = 50
platform_speed = 3

x = 400
y = 300 + table_height
ball_radius = 10
dot_speed = 2

move = randint(1, 4)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(0, 0, 800, 100))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x1, y1, 20, 80))
    pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(x2, y2, 20, 80))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), radius=ball_radius)

    f1 = pygame.font.Font(None, 86)
    text1 = f1.render('СЧЁТ', True, (0, 0, 0))
    screen.blit(text1, (320, 3))

    f2 = pygame.font.Font(None, 76)
    text2 = f2.render(f'0:0', True, (0, 0, 0))
    screen.blit(text2, (365, 55))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y1 -= platform_speed
    if pressed[pygame.K_DOWN]: y1 += platform_speed
    if pressed[pygame.K_w]: y2 -= platform_speed
    if pressed[pygame.K_s]: y2 += platform_speed

    if y1 > 520 + table_height: y1 = 520 + table_height
    if y1 < 0 + table_height: y1 = 0 + table_height
    if y2 > 520 + table_height: y2 = 520 + table_height
    if y2 < 0 + table_height: y2 = 0 + table_height

    match move:
        case 1:
            up_left()
        case 2:
            up_right()
        case 3:
            down_left()
        case 4:
            down_right()

    # Отталкивание от стенок по y
    if y - ball_radius - table_height <= 0 and move == 1:
        move = 3
    if y + ball_radius - table_height >= 600 and move == 3:
        move = 1
    if y - ball_radius - table_height <= 0 and move == 2:
        move = 4
    if y + ball_radius - table_height >= 600 and move == 4:
        move = 2

    # Отталкивание от стенок по x
    if x + ball_radius >= 800 and move == 2:
        move = 1
    if x - ball_radius <= 0 and move == 1:
        move = 2
    if x + ball_radius >= 800 and move == 4:
        move = 3
    if x - ball_radius <= 0 and move == 3:
        move = 4

    # Отталкивание от синей панели
    if x1 <= x + ball_radius <= x1 + 20 and move == 2 and y1 <= y <= y1 + 80:
        move = 1
    if x1 <= x + ball_radius <= x1 + 20 and move == 4 and y1 <= y <= y1 + 80:
        move = 3
    # Отталкивание от красной панели
    if x2 <= x - ball_radius <= x2 + 20 and move == 1 and y2 <= y <= y2 + 80:
        move = 2
    if x2 <= x - ball_radius <= x2 + 20 and move == 3 and y2 <= y <= y2 + 80:
        move = 4

    pygame.display.flip()
    clock.tick(60)
