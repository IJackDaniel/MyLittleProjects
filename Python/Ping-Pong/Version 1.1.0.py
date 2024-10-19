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


def start_game():
    global x, y, x1, y1, x2, y2, score1, score2, screen_color

    if score1 > score2:
        table_color = "orange"
    elif score2 > score1:
        table_color = "light blue"
    else:
        table_color = (200, 200, 200)

    screen.fill(screen_color)
    pygame.draw.rect(screen, table_color, pygame.Rect(0, 0, 800, table_height))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x1, y1, platform_width, platform_height))
    pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(x2, y2, platform_width, platform_height))
    pygame.draw.circle(screen, (255, 255, 255), (x, y), radius=ball_radius)

    f1 = pygame.font.Font(None, 86)
    text1 = f1.render('СЧЁТ', True, (0, 0, 0))
    screen.blit(text1, (320, 3))

    f2 = pygame.font.Font(None, 76)
    text2 = f2.render(f'{score1}:{score2}', True, (0, 0, 0))
    screen.blit(text2, (365, 55))


table_height = 100
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600 + table_height))  # flags=pygame.NOFRAME
screen_color = (30, 30, 30)
screen.fill(screen_color)
pygame.display.set_caption("Ping-Pong")
icon = pygame.image.load(r"images/icon.png")
pygame.display.set_icon(icon)

done = False

platform_height = 80  # 80
platform_width = 20  # 20
y1 = 300 - (platform_height // 2) + table_height
x1 = 750 - platform_width
y2 = 300 - (platform_height // 2) + table_height
x2 = 50
platform_speed = 5


x = 400
y = 300 + table_height
ball_radius = 10
dot_speed = 2

score1 = 0
score2 = 0

move = randint(1, 4)

i = 1
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    start_game()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y1 -= platform_speed
    if pressed[pygame.K_DOWN]: y1 += platform_speed
    if pressed[pygame.K_w]: y2 -= platform_speed
    if pressed[pygame.K_s]: y2 += platform_speed

    if pressed[pygame.K_g]: dot_speed += 1

    if pressed[pygame.K_p]: platform_height = 600
    if pressed[pygame.K_o]: platform_height = 80

    if pressed[pygame.K_r]:
        y1 = 300 - (platform_height // 2) + table_height
        x1 = 750 - platform_width
        y2 = 300 - (platform_height // 2) + table_height
        x2 = 50

        x = 400
        y = 300 + table_height

        score1 = 0
        score2 = 0

        move = randint(1, 4)

        dot_speed = 2

        continue

    if x > 770:  # 750 - platform_width
        score1 += 1
        x = 400
        y = 300
        move = randint(0, 1) * 2 + 1
        dot_speed = 2
    elif x < 30:  # 50 + platform_width
        score2 += 1
        x = 400
        y = 400
        move = randint(1, 2) * 2
        dot_speed = 2

    if y1 > 600 - platform_height + table_height: y1 = 600 - platform_height + table_height
    if y1 < 0 + table_height: y1 = 0 + table_height
    if y2 > 600 - platform_height + table_height: y2 = 600 - platform_height + table_height
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
    if x1 <= x + ball_radius <= x1 + platform_width and move == 2 and y1 <= y <= y1 + platform_height:
        move = 1
    if x1 <= x + ball_radius <= x1 + platform_width and move == 4 and y1 <= y <= y1 + platform_height:
        move = 3
    # Отталкивание от красной панели
    if x2 <= x - ball_radius <= x2 + platform_width and move == 1 and y2 <= y <= y2 + platform_height:
        move = 2
    if x2 <= x - ball_radius <= x2 + platform_width and move == 3 and y2 <= y <= y2 + platform_height:
        move = 4

    i += 1

    if i % 10 == 0:
        dot_speed += 0.03

    pygame.display.flip()
    clock.tick(60)
