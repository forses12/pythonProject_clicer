import pygame,sprite

class Button:
    def __init__(self,where,size,what):
        self.q=sprite.Sprite(what,size,where)

    def painter(self):
        self.q.printer()
        pygame.draw.rect(pygame.display.get_surface(), [31, 245, 99], pygame.rect.Rect([40, 40], [40, 60]), 1)
    def events(self,event):
        b=pygame.rect.Rect(self.q.where,[self.q.size,self.q.size])



        for e in event:
            if e.type == pygame.MOUSEBUTTONDOWN and b.collidepoint(e.pos):
                print('qazzwexsrcdtvfygbhnujmik,o')



