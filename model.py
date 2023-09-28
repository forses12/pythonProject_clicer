import pygame, writer,button

a = pygame.Rect([943, 10], [50, 50])
level_up_price = 10

n = writer.Writer('у вас есть ', ' монет', 0, 0)
l = writer.Writer('ЦЕНА УЛУЧШЕНИЯ ', ' ', 750, 60, num=10)
k = writer.Writer('level ', ' ', 10, 525, )
how_many_get_coin = writer.Writer('сколько дает клик ', ' ', 0, 735, num=2)
how_many_up = writer.Writer('+', ' ',1000,20,num=2)
j=button.Button([500,500],50,'sprites/controls/up_green.png')

def model():
    # print(n.my_color)
    pass


def up_coin():
    if n.number >= l.number:
        n.number -= l.number
        l.number *= 1.05

        how_many_get_coin.number += how_many_up.number

        k.number += 1
        how_many_up.number += 2


def get_coin():
    n.number += how_many_get_coin.number
