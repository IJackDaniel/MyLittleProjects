import pygame
from random import choice


# Инициализируем игру
pygame.init()
clock = pygame.time.Clock()

# Создаём окно, размером 1200x800
screen = pygame.display.set_mode((1200, 800))

# Работа с фоном. Будет два объекта, которые будут перемещаться со скоростью speed.
# Как только первый левый объект выйдет из окна, он переместиться вправо.
# Это позволит создать бесконечно сменяющуюся картинку фона
background1 = pygame.image.load("images/background.png")
back_x1 = 0
back_x2 = 1200
speed = 10

# загружаем фото png для динозаврика и меняем его размер
dino1 = pygame.image.load("images/dino1.png").convert_alpha()
dino2 = pygame.image.load("images/dino2.png").convert_alpha()
dino3 = pygame.image.load("images/dino3.png").convert_alpha()
dino4 = pygame.image.load("images/dino4.png").convert_alpha()
dino5 = pygame.image.load("images/dino5.png").convert_alpha()
dino1 = pygame.transform.scale(dino1, (150, 150))
dino2 = pygame.transform.scale(dino2, (150, 150))
dino3 = pygame.transform.scale(dino3, (150, 150))
dino4 = pygame.transform.scale(dino4, (150, 150))
dino5 = pygame.transform.scale(dino5, (150, 150))
fdino1 = pygame.image.load("images/fdino1.png").convert_alpha()
fdino2 = pygame.image.load("images/fdino2.png").convert_alpha()
fdino3 = pygame.image.load("images/fdino3.png").convert_alpha()
fdino4 = pygame.image.load("images/fdino4.png").convert_alpha()
fdino5 = pygame.image.load("images/fdino5.png").convert_alpha()
fdino1 = pygame.transform.scale(fdino1, (150, 150))
fdino2 = pygame.transform.scale(fdino2, (150, 150))
fdino3 = pygame.transform.scale(fdino3, (150, 150))
fdino4 = pygame.transform.scale(fdino4, (150, 150))
fdino5 = pygame.transform.scale(fdino5, (150, 150))
# dino = [dino1, dino1, dino2, dino2, dino3, dino3, dino4, dino4, dino5, dino5]
# fail_dino = [fdino1, fdino1, fdino2, fdino2, fdino3, fdino3, fdino4, fdino4, fdino5, fdino5]
dino = [dino1, dino1, dino1, dino2, dino2, dino2, dino3, dino3, dino3, dino4, dino4, dino4, dino5, dino5, dino5]
fail_dino = [fdino1, fdino1, fdino1, fdino2, fdino2, fdino2,
             fdino3, fdino3, fdino3, fdino4, fdino4, fdino4, fdino5, fdino5, fdino5]
n_dino = 0
# Параметры динозаврика:
# y - координата y динозаврика, которая нужна будет при прыжке
# is_jump, jump - отвечают за высоту прыжка
y = 500
is_jump = False
jump = 20
jump_height = 20  # Нужен для ограничений и не изменяется. Обязательно равен значению jump

# Загрузка фото для препятствия
ob1 = pygame.image.load("images/obstacle1.png").convert_alpha()
ob2 = pygame.image.load("images/obstacle2.png").convert_alpha()
ob3 = pygame.image.load("images/obstacle3.png").convert_alpha()
ob4 = pygame.image.load("images/obstacle4.png").convert_alpha()
ob5 = pygame.image.load("images/obstacle5.png").convert_alpha()
ob6 = pygame.image.load("images/obstacle6.png").convert_alpha()
ob1_2 = pygame.image.load("images/obstacle1_2.png").convert_alpha()
ob2_2 = pygame.image.load("images/obstacle2_2.png").convert_alpha()
ob3_2 = pygame.image.load("images/obstacle3_2.png").convert_alpha()
ob4_2 = pygame.image.load("images/obstacle4_2.png").convert_alpha()
ob5_2 = pygame.image.load("images/obstacle5_2.png").convert_alpha()
ob6_2 = pygame.image.load("images/obstacle6_2.png").convert_alpha()
# Массив со всеми объектами для будущего случайного выбора
obstacles_1 = [ob1, ob2, ob3, ob4, ob5, ob6]
obstacles_2 = [ob1_2, ob2_2, ob3_2, ob4_2, ob5_2, ob6_2]
obstacles = obstacles_1
# Массивы с различными размерами препятствий и соответствующими им координатами y
obs_height = 150
obs_y = 500
# Координата точки появления
x1 = 1250
# Флаг нахождения объекта на экране
x1_onScreen = False
# строчка "затычки", чтобы PyCharm не ругался
obs_num = 0


# счёт
score = 0

# done для закрытия окна, end для завершения игры при соприкосновении динозаврика с препятствием
done = False
end = False

# цикл игры
while not done:

    # Включение кнопки закрытия программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if not end:
        # Отрисовка заднего фона
        screen.blit(background1, (back_x1, 0))
        screen.blit(background1, (back_x2, 0))

        f = pygame.font.Font(None, 40)
        text_score = f.render(f"score: {score}", True, (0, 0, 0))
        screen.blit(text_score, (1000, 30))

        text_speed = f.render(f"speed: {round(speed, 2)}", True, (0, 0, 0))
        screen.blit(text_speed, (1000, 55))

        # Препятствия
        # Если координата в пределах экрана +- 50-100 пикселей и x1_onScreen == False
        if -100 <= x1 <= 1250 and not x1_onScreen:

            if speed >= 15:
                obstacles = obstacles_2
                obs_height = 250
                obs_y = 400

            x1_onScreen = True
            obs_num = choice(obstacles)  # выбор случайного препятствия
            obs_num = pygame.transform.scale(obs_num, (obs_height, obs_height))  # изменение размеров препятствия

        if x1 < -200:
            x1_onScreen = False

        if x1_onScreen:
            screen.blit(obs_num, (x1, obs_y))
            x1 -= speed
        else:
            x1 = 1250
            score += 1

        # Анимация дино
        screen.blit(dino[n_dino], (50, y))  # box ( x: 50 - 200  ;  y: y - y + 150 )

        # Столкновение
        if (50 <= x1 + obs_height // 2 <= 200 or 50 <= x1 <= 200) and y + 150 > obs_y:
            end = True
            screen.blit(fail_dino[n_dino], (50, y))

        n_dino += 1
        if n_dino == 15:
            n_dino = 0

    pressed = pygame.key.get_pressed()

    if end:
        # Если игра остановилась, и нажата клавиша "r", то игра начинается сначала
        if pressed[pygame.K_r]:
            end = False
            is_jump = False
            speed = 10
            score = 0
            jump = 20
            jump_height = 20
            back_x1 = 0
            back_x2 = 1200
            y = 500
            x1 = 1250
            n_dino = 0
            obstacles = obstacles_1
            continue

    if not end:
        # Прыжок
        if not is_jump:
            if pressed[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump >= -jump_height:
                if jump > 0:
                    y -= (jump ** 2) // 6
                else:
                    y += (jump ** 2) // 6
                jump -= 1
            else:
                jump = jump_height
                is_jump = False

        ####### НУЖНО ТОЛЬКО ДЛЯ ТЕСТОВ
        if pressed[pygame.K_UP]:
            y -= 5
        if pressed[pygame.K_DOWN]:
            y += 5
        if pressed[pygame.K_q]:
            y = 500
        #######

        # Смещение фона
        back_x1 -= speed
        back_x2 -= speed
        if back_x1 <= -1200:
            back_x1 = 1200
        if back_x2 <= -1200:
            back_x2 = 1200

        if speed <= 30:
            speed += 0.002
            speed = round(speed, 3)

    pygame.display.flip()
    clock.tick(60)
