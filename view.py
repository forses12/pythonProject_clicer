import pygame

pygame.init()

screen = pygame.display.set_mode([1200, 800])
font = pygame.font.SysFont('vinerhanditc', 50)
font1 = pygame.font.SysFont('comicsansms', 25)

import model, sprite, worker

first_place = sprite.Sprite('sprites/place/place1.jpg', 800, [0, 0])

rect = pygame.draw.rect(screen, [255, 255, 255], model.a)


# h.cozdavatel()
worker = sprite.Sprite('sprites/worker/worker1.png', 240, [30, 570])


def draw():
    first_place.printer()

    model.n.paint()
    model.l.paint()

    model.coin_in_second.paint()

    model.level_bomga.paint()

    worker.printer()
    model.business.painter()
    model.worker3.painter()
    model.worker2.painter()

    model.up_level1.painter()

    model.how_many_get_coin_for_up.paint()

    model.how_many_up.paint()
    pygame.display.flip()
