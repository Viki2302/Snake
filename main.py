"""
Инструкция к игре Змейка.

В игре змейка есть 3 уровня игры.
1 уровень. Легкий
2 уровень. Добавляется скорость змейки после съеденного яблока
3 уровень. Добавляется вторая змейка, которая может укусить

Во время игры:
Пауза в игре осуществляется кнопкой Esc

Игра закончена:
При столкновение со стеной.
При столкновение с телом змейки
"""

import pygame
import random
import pygame_menu

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102, 1)
black = (0, 0, 0)
red = (255, 36, 0)
green = (0, 165, 80)
blue = (50, 153, 213)

# окно
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))

# заголовок
pygame.display.set_caption('Snake Game by Pythonist')

# скорость змейки
clock = pygame.time.Clock()

# координата змейки для рисунка
snake_block = 20

# стиль для текста
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# уровень игры
medium = True
complex = True
def set_difficulty(value, difficulty):
    global medium
    global complex
    if difficulty == 2:
        medium = False
        complex = True
    elif difficulty == 1:
        complex = False
        medium = False
    else:
        medium = True
        complex = True

def start_the_game():

    def you_score(score):
        value = score_font.render("Ваш Счет: " + str(score), True, yellow)
        dis.blit(value, [0, 0])

    # cоздание змейки
    def our_snake(snake_block, snake_list, green_snake):
        for x in snake_list:
            pygame.draw.rect(dis, green_snake, [x[0], x[1], snake_block, snake_block])

    def gameLoop():

        # скорость змейки
        snake_speed = 5

        game_over = False
        game_close = False

        # координаты змейки
        x1 = dis_width / 2
        y1 = dis_height / 2
        x1_change = 0
        y1_change = 0

        # длина змеи
        snake_List = [[x1, y1]]
        Length_of_snake = 2

        x2 = dis_width / 3  # вторая змея
        y2 = dis_height / 2
        snake_List2 = [[x2 - 60, y2 - 60], [x2 - 40, y2 - 40], [x2 - 20, y2 - 20]]

        # координаты яблока
        foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
        foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0

        # змейка не может двигаться в сторону хвоста
        dirs = {"L": True, "R": True, "U": True, "D": True}

        global oyunOyna
        oyunOyna = False

        while not game_over:

            while game_close == True:
                menu.mainloop(dis)

            for event in pygame.event.get():  # цикл обработки событий
                if event.type == pygame.QUIT:  # если тип событие выход
                    game_over = True
                if event.type == pygame.KEYDOWN:  # если тип события нажатие клавиш
                    if event.key == pygame.K_LEFT and dirs["L"]:  # левая клавиша
                        x1_change = -snake_block
                        y1_change = 0
                        dirs = {"L": True, "R": False, "U": True, "D": True}
                    elif event.key == pygame.K_RIGHT and dirs["R"]:  # правая клавиша
                        x1_change = snake_block
                        y1_change = 0
                        dirs = {"L": False, "R": True, "U": True, "D": True}
                    elif event.key == pygame.K_UP and dirs["U"]:  # верхняя клавиша
                        y1_change = -snake_block
                        x1_change = 0
                        dirs = {"L": True, "R": True, "U": True, "D": False}
                    elif event.key == pygame.K_DOWN and dirs["D"]:  # нижняя клавиша
                        y1_change = snake_block
                        x1_change = 0
                        dirs = {"L": True, "R": True, "U": False, "D": True}

                    # Пауза в игре
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            oyunOyna = True
                            while oyunOyna == True:
                                durduruldu_text = font_style.render('  Пауза в игре  ', True, red)
                                dis.blit(durduruldu_text, [dis_width / 3, dis_height / 3])
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            oyunOyna = False

            # увеличение координаты перемещения змейки
            x1 += x1_change
            y1 += y1_change

            # автоматическое перемещение змеи
            if Length_of_snake < 3 and dirs["D"] == True and dirs["L"] == True and dirs["U"] == True and dirs["R"] == True:
                x1 -= snake_block

            # когда змейка уходит за границы окна
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

            # цвет фона окна
            dis.fill(black)

            # рисуем яблоко
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

            # в старую координату добавляем новую
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)

            # если элементов в старом списке больше чем количество клеток
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            # вторая змея
            snake_Head2 = []
            snake_Head2.append(x2)
            snake_Head2.append(y2)
            snake_List2.append(snake_Head2)

            i = random.randint(1, 4)
            d = {"1": True, "2": True, "3": True, "4": True}

            if i == 1 and x2 != 0 and y2 != dis_height and d["1"] == True:
                x2 -= snake_block
                y2 += snake_block
                d = {"1": True, "2": False, "3": True, "4": True}
            if i == 2 and x2 != dis_width and y2 != 0 and d["2"] == True:
                x2 += snake_block
                y2 -= snake_block
                d = {"1": False, "2": True, "3": True, "4": True}
            if i == 3 and x2 != 0 and y2 != 0 and d["3"] == True:
                x2 -= snake_block
                y2 -= snake_block
                d = {"1": True, "2": True, "3": True, "4": False}
            if i == 4 and x2 != dis_width and y2 != dis_height and d["4"] == True:
                x2 += snake_block
                y2 += snake_block
                d = {"1": True, "2": True, "3": False, "4": True}

            if len(snake_List2) > 4:
                del snake_List2[0]

            if not complex:
                our_snake(snake_block, snake_List2, yellow)

            # функция змеи
            our_snake(snake_block, snake_List, green)

            you_score(Length_of_snake-2)

            # применение каких то изменений на экране
            pygame.display.update()

            # координата змейки равна координате яблока
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
                foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
                Length_of_snake += 1

                if not medium:
                    snake_speed = snake_speed + 1

            # координата змейки 1 равна координате змейки 2
            if not complex:
                for x in snake_List:
                    if x[0] == x2 and x[1] == y2:
                        game_close = True

            clock.tick(snake_speed)

        pygame.quit()
        quit()
    gameLoop()

menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)
menu.add.text_input('Имя игрока :', default='Игрок')
menu.add.selector('Уровень :', [('Легкий', 3), ('Средний', 2), ('Сложный', 1)], onchange=set_difficulty)
menu.add.button('Играть', start_the_game)
menu.add.button('Выход', pygame_menu.events.EXIT)

menu.mainloop(dis)
