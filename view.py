import pygame

pygame.init()

screen = pygame.display.set_mode([1200, 800])
font = pygame.font.SysFont('vinerhanditc', 50)
font1 = pygame.font.SysFont('comicsansms', 25)

import model, sprite




first_place = pygame.transform.scale(pygame.image.load('sprites/place/place1.jpg'), [1200, 800])
up_level = pygame.transform.scale(pygame.image.load('sprites/controls/up_green.png'), [50, 50])
bomge = pygame.transform.scale(pygame.image.load('sprites/worker/worker1.png'),[613/714*200,200])
worker= pygame.transform.scale(pygame.image.load('sprites/worker/worker2.png'),[730/1033*400,400])
rect = pygame.draw.rect(screen, [255, 255, 255], model.a)
h = sprite.Sprite('sprites/worker/worker2.png', [300, 300], [400, 400])
# h.cozdavatel()




def draw():
    screen.blit(first_place, [0, 0])
    screen.blit(up_level, [943, 10])
    screen.blit(bomge,[10,550])
    screen.blit(worker,[120,280])

    model.n.paint()
    model.l.paint()
    model.k.paint()
    h.printer()
    model.how_many_get_coin.paint()
    model.how_many_up.paint()
    pygame.display.flip()
