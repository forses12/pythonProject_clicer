import pygame

pygame.init()
print(pygame.font.get_fonts())
screen=pygame.display.set_mode([1200,800])
font=pygame.font.SysFont('vinerhanditc',50)

import model
first_place=pygame.image.load('sprites/place/place1.jpg')
up_level=pygame.image.load('sprites/controls/up_green.png')
first_place_1=pygame.transform.scale(first_place,[1200,800])
up_level_1=pygame.transform.scale(up_level,[50,50])
def draw():
    picture = font.render(str(model.coin), True, [255,255,255])
    screen.blit(first_place_1,[0,0])
    screen.blit(up_level_1,[943,10])
    screen.blit(picture,[1000,0])
    pygame.display.flip()
