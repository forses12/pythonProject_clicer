import pygame

screen=pygame.display.get_surface()

class Sprite:
    def __init__(self,what,size,where):
        self.what=what
        self.size=size
        self.where=where
        self.l=pygame.image.load(self.what)
        self.picture= pygame.transform.scale(self.l,[self.l.get_width()/self.l.get_height()*size,size])

    def printer(self):
        pass
        screen.blit(self.picture,self.where)


