import pygame

screen=pygame.display.get_surface()

class Sprite:
    def __init__(self,what,size,where):
        self.what=what
        self.size=size
        self.where=where
        self.picture= pygame.transform.scale(pygame.image.load(self.what),self.size)

    def printer(self):
        pass
        screen.blit(self.picture,self.where)

