import pygame

pygame.init()

screen = pygame.display.set_mode([1200, 800])
font = pygame.font.SysFont('vinerhanditc', 50)
font1 = pygame.font.SysFont('comicsansms', 25)

import model, sprite




first_place = sprite.Sprite('sprites/place/place1.jpg',800,[0,0])

up_level = pygame.transform.scale(pygame.image.load('sprites/controls/up_green.png'), [50, 50])
rect = pygame.draw.rect(screen, [255, 255, 255], model.a)
worker1 = sprite.Sprite('sprites/worker/worker2.png',400,[300, 300])
# h.cozdavatel()
worker=sprite.Sprite('sprites/worker/worker1.png',240,[30,570])





def draw():
    first_place.printer()

    screen.blit(up_level, [943, 10])


    model.n.paint()
    model.l.paint()
    model.k.paint()
    worker1.printer()
    worker.printer()
    model.j.painter()

    model.how_many_get_coin.paint()
    model.how_many_up.paint()
    pygame.display.flip()
