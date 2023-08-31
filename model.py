import pygame

coin = 0
a = pygame.Rect([943, 10], [50, 50])
c = 2
how_many_up = 2
level_up_price = 10


def model():
    pass


def up_coin():
    global c, coin, level_up_price, how_many_up
    if coin >= level_up_price:
        coin -= level_up_price
        c += how_many_up
        how_many_up += 2
        level_up_price *= 1.05


def get_coin():
    global coin
    coin += c
