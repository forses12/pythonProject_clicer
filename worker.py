import pygame,control

import sprite,button
import writer


class Worker:
    def __init__(self, who, where, size):
        self.who = who
        self.where = where
        self.size = size
        self.l = sprite.Sprite(self.who, self.size, self.where)
        self.level_worker = 0

        self.f = writer.Writer('level ', '', self.where[0] + 30, self.where[1] - 30, num=self.level_worker)
        self.j=button.Button([self.where[0]+80,self.where[1]+70],50,'sprites/controls/up_green.png',self.level)

    def painter(self):
        self.l.printer()
        self.f.paint()
        self.button()

    def level(self):
        print(1234567777777777777)


    def button(self):
        self.j.painter()



