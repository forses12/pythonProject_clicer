import pygame

import sprite
import writer


class Worker:
    def __init__(self, who, where, size):
        self.who = who
        self.where = where
        self.size = size
        self.l = sprite.Sprite(self.who, self.size, self.where)
        self.level_worker = 0
        self.f = writer.Writer('level ', '', self.where[0] + 30, self.where[1] - 30, num=self.level_worker)

    def painter(self):
        self.l.printer()
        self.level()

    def level(self):
        self.f.paint()
