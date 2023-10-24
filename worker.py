import pygame

import sprite


class Worker:
    def __init__(self,who,where,size):
        self.who=who
        self.where=where
        self.size=size
    def painter(self):
        l=sprite.Sprite(self.who,self.size,self.where)
        sprite.Sprite.printer()