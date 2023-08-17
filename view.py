import pygame

screen=pygame.display.set_mode([1200,800])

import model

first_place=pygame.image.load('sprites/place/place1.jpg')
first_place_1=pygame.transform.scale(first_place,[1200,800])
def draw():
    screen.blit(first_place_1,[0,0])
    pygame.display.flip()
