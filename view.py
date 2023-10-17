import pygame

pygame.init()

screen = pygame.display.set_mode([1200, 800])
font = pygame.font.SysFont('vinerhanditc', 50)
font1 = pygame.font.SysFont('comicsansms', 25)

import model, sprite




first_place = sprite.Sprite('sprites/place/place1.jpg',800,[0,0])


rect = pygame.draw.rect(screen, [255, 255, 255], model.a)
worker1 = sprite.Sprite('sprites/worker/worker2.png',400,[300, 300])
# h.cozdavatel()
worker=sprite.Sprite('sprites/worker/worker1.png',240,[30,570])





def draw():
    first_place.printer()





    model.n.paint()
    model.l.paint()
    model.l1.paint()
    model.coin_in_second.paint()
    model.level_bomga.paint()
    model.level_worker1.paint()
    worker1.printer()
    worker.printer()
    model.up_level.painter()
    model.up_level1.painter()

    model.how_many_get_coin.paint()
    model.how_many_up.paint()
    pygame.display.flip()
