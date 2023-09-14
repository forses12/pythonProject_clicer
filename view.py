import pygame, writer

pygame.init()

screen = pygame.display.set_mode([1200, 800])
font = pygame.font.SysFont('vinerhanditc', 50)
font1 = pygame.font.SysFont('comicsansms', 25)

import model

first_place = pygame.image.load('sprites/place/place1.jpg')
up_level = pygame.image.load('sprites/controls/up_green.png')
first_place_1 = pygame.transform.scale(first_place, [1200, 800])
up_level_1 = pygame.transform.scale(up_level, [50, 50])
rect = pygame.draw.rect(screen, [255, 255, 255], model.a)




def draw():
    have_coin = font.render(str(int(model.coin)), True, [255, 255, 255])
    how_many_get_coin = font1.render(('сколько даёт клик ' + str(model.c)), True, [0, 255, 255])
    price1 = font1.render(('цена улучшения ' + str(int(model.level_up_price))), True, [0, 255, 255])
    how_many_up = font1.render(('+ ' + str(int(model.how_many_up))), True, [0, 255, 255])


    screen.blit(first_place_1, [0, 0])
    screen.blit(up_level_1, [943, 10])
    screen.blit(have_coin, [1000, 0])
    screen.blit(how_many_get_coin, [0, 0])
    screen.blit(price1, [700, 5])
    screen.blit(how_many_up, [700, 30])
    model.n.paint()
    model.l.paint()
    model.k.paint()
    pygame.display.flip()
