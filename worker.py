import pygame, control

import sprite, button
import writer


class Worker:
    def __init__(self, who, where, size, coin: writer.Writer,coin_in_second,price,sale,worker,visible,procent,procent_up):
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
        self.worker=worker

        self.visible=visible
        self.j = button.Button([self.where[0] + 80, self.where[1] + 70], 50, 'sprites/controls/up_green.png',
                                   self.level)

        self.price = writer.Writer('стоимость ', '', self.where[0] + 80, self.where[1] + 125, num=price)
        self.how_many_up_in_second = writer.Writer('даст:', ' монет', self.where[0] + 80, self.where[1] + 150, num=sale)
        self.sale=sale
        self.procent_coin_=procent
        self.procent_coin__up=procent_up
    def event(self,event):
        if self.visible:
            self.j.events(event)



    def painter(self):
        if self.visible:
            self.l.printer()
            self.f.paint()
            self.button()

    def level(self):

        if self.coin.number>=self.price.number:
            self.coin.number-=self.price.number
            self.f.number += 1
            if self.worker!=None and self.f.number>=10:
                self.worker.visible=True
            if self.f.number==20:
                self.procent_coin_[0]+=self.procent_coin__up
            self.price.number*=self.procent
            self.procent+=0.02283
            self.coin_in_second.number+=self.how_many_up_in_second.number
            self.how_many_up_in_second.number=self.sale*(self.f.number+1)
            if self.f.number > 0:
                self.who = self.who.replace('_inv', '')
                self.l = sprite.Sprite(self.who, self.size, self.where)

    def button(self):
        self.price.paint()

        self.how_many_up_in_second.paint()
        self.j.painter()
