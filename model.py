import pygame, writer,button,worker
j=1.02
h=0
procent=[1]

def model():
        n.number+=coin_in_second.number




def up_coin():
    if n.number >= l.number:
        n.number -= l.number
        l.number *= 1.05

        how_many_get_coin.number += how_many_up.number
        how_many_get_coin_for_up.number=how_many_get_coin.number*procent[0]

        level_bomga.number += 1
        how_many_up.number += 2




def get_coin():

    n.number +=how_many_get_coin_for_up.number



a = pygame.Rect([943, 10], [50, 50])
level_up_price = 10

n = writer.Writer('у вас есть ', ' монет', 0, 0, num=10000000)
l = writer.Writer('стоит ', ' ', 950, 60, num=10)
coin_in_second=writer.Writer('доход в секунду:',' монет',0,20)
level_bomga = writer.Writer('level ', ' ', 10, 525, )
how_many_get_coin = writer.Writer('сколько дает клик ', ' ',880, 730, num=2)
how_many_get_coin_for_up = writer.Writer('сколько дает клик  с улучшением ', ' ',600, 730, num=2)



how_many_up = writer.Writer('+', ' ',1000,20,num=2)

up_level1 = button.Button([943, 10],50,'sprites/controls/up_green.png',up_coin)
worker3 = worker.Worker('sprites/worker/worker3_inv.png', [400, 500], 200,n,coin_in_second,50000,10,None,False,procent,0.3)
worker2=worker.Worker('sprites/worker/worker2_inv.png', [250,350], 300,n,coin_in_second,10000,2,worker3,True,procent,0.2)
