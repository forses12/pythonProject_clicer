import pygame,sprite

class Button:
    def __init__(self,where,size,what,work):
        self.q=sprite.Sprite(what,size,where)
        self.rect=pygame.rect.Rect(self.q.where,self.q.picture.get_size())
        self.width=0
        self.work=work

    def painter(self):
        self.q.printer()
        if self.width==1:
            self.b=pygame.draw.rect(pygame.display.get_surface(), [31, 245, 99],self.rect,4)
    def events(self,event):



        for e in event:
            if e.type == pygame.MOUSEMOTION and self.rect.collidepoint(e.pos):
                self.width=1

            else:
                self.width=0

            if e.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(e.pos):
                self.work()
                event.remove(e)



