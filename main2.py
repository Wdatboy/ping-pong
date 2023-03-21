import pygame
import random
from time import sleep

pygame.init()

w_width = 1000
w_height = 500

pygame.display.set_caption("PING PONG")

w_size = (w_width, w_height)

window = pygame.display.set_mode(w_size)

speed_x, speed_y = 0.2, 0.2

pad_x, pad_y = 25, w_height // 2 - w_height // 6

pad2_x, pad2_y = 940, w_height // 2 - w_height // 6

paddle1 = (pad_x, pad_y)

paddle2 = (pad2_x, pad2_y)

ball_x, ball_y = w_width // 2, w_height // 2

dir_x = random.choice((-1, 1))
dir_y = random.choice((-1, 1))

font = pygame.font.Font(None, max(w_width, w_height) // 10)

flag = True

count_left = 0
count_right = 0

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    ball_x_speed = 0.2 * dir_x
    ball_y_speed = 0.2 * dir_y
    ball_x += ball_x_speed
    ball_y += ball_y_speed
    window.fill((0, 255, 0))

    pygame.draw.line(window, (255, 255, 255), [w_width // 2, 0], [w_width // 2, w_height], 5)
    pygame.draw.circle(window, (255, 255, 255), (w_width // 2, w_height // 2), 15)

    text_surface = font.render(f'score: {count_left} : {count_right}', False, (0, 0, 0))
    window.blit(text_surface, (w_width // 2 - 200, 5))
    pygame.draw.circle(window, (0, 0, 0), (ball_x, ball_y), 15)
    pygame.draw.rect(window, (0, 0, 0), (pad_x, pad_y, w_width // 30, w_height // 3))
    pygame.draw.rect(window, (0, 0, 0), (pad2_x, pad2_y, w_width // 30, w_height // 3))
    if count_left == 5:
        pygame.display.update()
        text_surface = font.render('LEFT WIN!', False, (0, 0, 0))
        window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
        pygame.display.update()
        sleep(2)
        game_over = True
    if count_right == 5:
        pygame.display.update()
        text_surface = font.render('RIGHT WIN!', False, (0, 0, 0))
        window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
        pygame.display.update()
        sleep(2)
        game_over = True
    if count_right == 4 and count_left == 4:
        pygame.display.update()
        text_surface = font.render('DRAW!', False, (0, 0, 0))
        window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
        pygame.display.update()
        sleep(2)
        game_over = True
    pygame.display.update()
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if not (pad_y <= 0):
            pad_y -= speed_y
    if key[pygame.K_s]:
        if not (pad_y >= w_height - w_height // 3):
            pad_y += speed_y
    if key[pygame.K_UP]:
        if not (pad2_y <= 0):
            pad2_y -= speed_y
    if key[pygame.K_DOWN]:
        if not (pad2_y >= w_height - w_height // 3):
            pad2_y += speed_y
    if count_left == 5:
        pygame.display.update()
        text_surface = font.render('LEFT WIN!', False, (0, 0, 0))
        window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
        pygame.display.update()
        sleep(2)
        game_over = True
    if count_right == 5:
        pygame.display.update()
        text_surface = font.render('RIGHT WIN!', False, (0, 0, 0))
        window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
        pygame.display.update()
        sleep(2)
        game_over = True
    if count_right == 4 and count_left == 4:
        pygame.display.update()
        text_surface = font.render('DRAW!', False, (0, 0, 0))
        window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
        pygame.display.update()
        sleep(2)
        game_over = True
    if ball_y >= w_height - 8:
        dir_y = -1
    if ball_y <= 8:
        dir_y = 1
    if (ball_y and ball_x) >= (pad2_y and pad2_x):
        if ball_y >= pad2_y - 15 and ball_y <= pad2_y + w_height // 3 - 15:
            dir_x = -1
    if (ball_y and ball_x) <= (pad_y and pad_x + w_width // 30):
        if ball_y >= pad_y + 15 and ball_y <= pad_y + w_height // 3 - 15:
            dir_x = 1
    if ball_x <= 0 or ball_x - 15 >= w_width:
        if ball_x + 15 <= 0:
            count_right += 1
            text_surface = font.render('LEFT LOST!', False, (0, 0, 0))
            window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
            pygame.display.update()
            ball_x, ball_y = w_width // 2, w_height // 2
            pad_x, pad_y = 25, w_height // 2 - w_height // 6
            pad2_x, pad2_y = 940, w_height // 2 - w_height // 6
            sleep(2)
        if ball_x >= w_width:
            count_left += 1
            text_surface = font.render('RIGHT LOST!', False, (0, 0, 0))
            window.blit(text_surface, (w_width // 2 - w_width // 5, w_height // 2 - w_width // 20))
            pygame.display.update()
            ball_x, ball_y = w_width // 2, w_height // 2
            pad_x, pad_y = 25, w_height // 2 - w_height // 6
            pad2_x, pad2_y = 940, w_height // 2 - w_height // 6
            sleep(2)
# # Описание проекта `(project description)`
# # Русский
# Этот проект создаёт телеграмм бота, который выводит вам погоду через сайт world-weather.ru и переводит.
# # English
# This project creates a telegram bot that displays the weather for you through the world-weather.ru website and translates it.
# # Установка библиотек `(install libraries)`
# `pip install pytelegrambotapi`
#
# `pip install beautifulsoup4`
#
# `pip install requests`
#
# `pip install googletrans==3.1.0a0`