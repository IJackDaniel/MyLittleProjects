import pygame
from random import choice, randint


# Инициализируем игру
pygame.init()
# Пока не знаю для чего это!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
clock = pygame.time.Clock()

# Создаём окно, размером
screen = pygame.display.set_mode((1200, 800))

# Работа с фоном. Будет два объекта, которые будут перемещаться со скоростью speed.
# Как только первый левый объект выйдет из окна, он переместиться вправо.
# Это позволит создать бесконечно сменяющуюся картинку фона
background1 = pygame.image.load("images/background.png")
back_x1 = 0
back_x2 = 1200
speed = 15

# загружаем фото png для динозаврика и меняем его размер
dino = pygame.image.load("images/dino.png").convert_alpha()
dino = pygame.transform.scale(dino, (150, 150))
# Параметры динозаврика:
# y - координата y динозаврика, которая нужна будет при прыжке
# is_jump, jump - отвечают за высоту прыжка
y = 500
is_jump = False
jump = 14
jump_height = 14  # Нужен для ограничений и не изменяется. Обязательно равен значению jump

# Загрузка фото для препятствия
ob1 = pygame.image.load("images/obstacle1.png").convert_alpha()
ob2 = pygame.image.load("images/obstacle2.png").convert_alpha()
ob3 = pygame.image.load("images/obstacle3.png").convert_alpha()
ob4 = pygame.image.load("images/obstacle4.png").convert_alpha()
ob5 = pygame.image.load("images/obstacle5.png").convert_alpha()
ob6 = pygame.image.load("images/obstacle6.png").convert_alpha()
# Массив со всеми объектами для будущего случайного выбора
obstacles = [ob1, ob2, ob3, ob4, ob5, ob6]
# Массивы с различными размерами препятствий и соответствующими им координатами y
obstacles_height = [80, 100, 120]
obstacles_y = [580, 550, 530]
# Координата точки появления
x1 = 1250
# Флаг нахождения объекта на экране
x1_onScreen = False
# Три строчки "затычки", чтобы PyCharm не ругался
obs_num = 0
ob_h = 0
ob_y = 0

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
        screen.blit(text_score, (1000, 50))

        text_speed = f.render(f"speed: {round(speed, 2)}", True, (0, 0, 0))
        screen.blit(text_speed, (1000, 70))

        # Препятствия
        # Если координата в пределах экрана +- 50-100 пикселей и x1_onScreen == False
        if -100 <= x1 <= 1250 and not x1_onScreen:
            x1_onScreen = True
            obs_num = choice(obstacles)  # выбор случайного препятствия
            i = randint(0, 2)
            ob_y = obstacles_y[i]  # выбор размеров препятствия
            ob_h = obstacles_height[i]  # выбор координаты препятствия с учётом его размеров
            obs_num = pygame.transform.scale(obs_num, (ob_h, ob_h))  # изменение размеров препятствия

        if x1 < -100:
            x1_onScreen = False

        if x1_onScreen:
            screen.blit(obs_num, (x1, ob_y))
            x1 -= speed
        else:
            x1 = 1250
            score += 1

        # Анимация
        screen.blit(dino, (50, y))  # box ( x: 50 - 200  ;  y: y - y + 150 )

        # Столкновение
        if (50 <= x1 + ob_h <= 200 or 50 <= x1 <= 200) and y + 150 > ob_y:
            end = True

    pressed = pygame.key.get_pressed()

    if end:
        # Если игра остановилась, и нажата клавиша "r", то игра начинается сначала
        if pressed[pygame.K_r]:
            end = False
            is_jump = False
            speed = 15
            score = 0
            jump = 15
            jump_height = 15
            back_x1 = 0
            back_x2 = 1200
            y = 500
            x1 = 1250
            continue

    if not end:
        # Прыжок
        if not is_jump:
            if pressed[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump >= -jump_height:
                if jump > 0:
                    y -= (jump ** 2) // 4
                else:
                    y += (jump ** 2) // 4
                jump -= 1
            else:
                jump = jump_height
                is_jump = False

        ####### НУЖНО ТОЛЬКО ДЛЯ ТЕСТОВ
        if pressed[pygame.K_UP]:
            y -= 5
        if pressed[pygame.K_DOWN]:
            y += 5
        #######

        # Смещение фона
        back_x1 -= speed
        back_x2 -= speed
        if back_x1 <= -1200:
            back_x1 = 1200
        if back_x2 <= -1200:
            back_x2 = 1200

        if speed <= 25:
            speed += 0.001

    pygame.display.flip()
    clock.tick(60)
