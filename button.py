import pygame,sprite

class Button:
    def __init__(self,xy,size,what):
        self.q=sprite.Sprite(what,size,xy)

    def painter(self):
        self.q.printer()
    def events(self,event):
        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN and self.q.where[0]<=:
                print('zaqwesxrdctfvygbuhnijmok,lp.[;/')


