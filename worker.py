import pygame, control

import sprite, button
import writer


class Worker:
    def __init__(self, who, where, size, coin: writer.Writer,coin_in_second):
        self.who = who
        self.where = where
        self.size = size
        self.f = writer.Writer('level ', '', self.where[0] + 30, self.where[1] - 30, num=0)
        if self.f.number>0:
            self.who=self.who.replace('_inv','')

        self.l = sprite.Sprite(self.who, self.size, self.where)
        self.coin = coin
        self.coin_in_second=coin_in_second
        self.procent=1.02
        self.j = button.Button([self.where[0] + 80, self.where[1] + 70], 50, 'sprites/controls/up_green.png',
                               self.level)
        self.price = writer.Writer('стоимость ', '', self.where[0] + 80, self.where[1] + 125, num=50000)
        self.how_many_up_in_second = writer.Writer('даст:', ' монет', self.where[0] + 80, self.where[1] + 150, num=10)

    def painter(self):
        self.l.printer()
        self.f.paint()
        self.button()

    def level(self):

        if self.coin.number>=self.price.number:
            self.coin.number-=self.price.number
            self.f.number += 1
            self.price.number*=self.procent
            self.procent+=0.02283
            self.coin_in_second.number+=self.how_many_up_in_second.number
            self.how_many_up_in_second.number=10*(self.f.number+1)
            if self.f.number > 0:
                self.who = self.who.replace('_inv', '')
                self.l = sprite.Sprite(self.who, self.size, self.where)

    def button(self):
        self.price.paint()

        self.how_many_up_in_second.paint()
        self.j.painter()
