import pygame,writer

coin = 0
a = pygame.Rect([943, 10], [50, 50])
c = 2
how_many_up = 2
level_up_price = 10




n = writer.Writer('у вас есть ', ' монет', 300, 500)
l = writer.Writer('ЦЕНА УЛУЧШЕНИЯ ', ' ', 400, 400,num=10)
k = writer.Writer('level ', ' ', 500, 600,)



def model():
    print(n.my_color)
    pass


def up_coin():
    global c, level_up_price, how_many_up
    if n.number >= level_up_price:
        n.number -= level_up_price
        c += how_many_up
        how_many_up += 2
        level_up_price *= 1.05

        l.number=level_up_price
        k.number+=1




def get_coin():
    n.number+=c




