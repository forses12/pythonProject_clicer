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
    screen.blit(first_place_1, [0, 0])
    screen.blit(up_level_1, [943, 10])

    model.n.paint()
    model.l.paint()
    model.k.paint()
    model.how_many_get_coin.paint()
    model.how_many_up.paint()
    pygame.display.flip()
