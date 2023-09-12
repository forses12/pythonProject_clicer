import pygame,writer

coin = 0
a = pygame.Rect([943, 10], [50, 50])
c = 2
how_many_up = 2
level_up_price = 10



n = writer.Writer('у вас есть ', ' монет', 300, 500)
l = writer.Writer('ЦЕНА УЛУЧШЕНИЯ ', ' ', 400, 400,num=10)



def model():
    print(n.my_color)
    pass


def up_coin():
    global c, coin, level_up_price, how_many_up
    if coin >= level_up_price:
        coin -= level_up_price
        c += how_many_up
        how_many_up += 2
        level_up_price *= 1.05
        n.num = coin
        n.cozdavatel()
        l.num = level_up_price
        l.cozdavatel()
        n.my_color='white'



def get_coin():
    global coin
    coin += c
    n.num = coin
    n.cozdavatel()
    n.my_color='blue'




