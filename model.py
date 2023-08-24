import pygame

coin = 0
a = pygame.Rect([943, 10], [50, 50])
c = 2


def model():
    pass


def up_coin():
    global c,coin
    if coin >= 10:
        coin-=10
        c += 2


def get_coin():
    global coin
    coin+=c
