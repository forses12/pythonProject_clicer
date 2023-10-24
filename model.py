import pygame, writer,button
j=1.02
h=0
procent=1

def model():
    if h!=level_worker1.number:

        n.number+=coin_in_second.number



    pass


def up_coin():
    if n.number >= l.number:
        n.number -= l.number
        l.number *= 1.05

        how_many_get_coin.number += how_many_up.number
        how_many_get_coin_by_up.number = how_many_get_coin.number * procent

        level_bomga.number += 1
        how_many_up.number += 2
def up_worker():
    global j,h,procent
    if n.number>=l1.number:
        n.number-=l1.number
        level_worker1.number+=1
        how_many_up_in_second.number=level_worker1.number*2+2
        coin_in_second.number +=level_worker1.number*2

        if level_worker1.number==20:
            procent+=0.2
            how_many_get_coin_by_up.number = how_many_get_coin.number * procent
        l1.number*=j
        j+=0.02283




def get_coin():

    n.number += how_many_get_coin_by_up.number



a = pygame.Rect([943, 10], [50, 50])
level_up_price = 10

n = writer.Writer('у вас есть ', ' монет', 0, 0,num=10000000)
l = writer.Writer('стоит ', ' ', 950, 60, num=10)
l1 = writer.Writer('стоит ', ' ', 555,500, num=10000)
coin_in_second=writer.Writer('доход в секунду:',' монет',0,20)
how_many_up_in_second=writer.Writer('даст:',' монет',550,520,num=2)
level_bomga = writer.Writer('level ', ' ', 10, 525, )
level_worker1 = writer.Writer('level ', ' ', 300,250, )
how_many_get_coin = writer.Writer('сколько дает клик ', ' ',880, 730, num=2)
how_many_get_coin_by_up = writer.Writer('сколько дает клик с улучшением ', ' ',700,750, num=2)

how_many_up = writer.Writer('+', ' ',1000,20,num=2)
up_level=button.Button([500,500],50,'sprites/controls/up_yellow.png',up_worker)
up_level1 = button.Button([943, 10],50,'sprites/controls/up_green.png',up_coin)
