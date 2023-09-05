import pygame

pygame.init()
font = pygame.font.SysFont('comicsansms', 50)


class Writer:
    def __init__(self, str_l,str_r, x, y,num=0):
        self.str_l = str_l
        self.str_r = str_r
        self.x = x
        self.y = y
        self.num = num
        self.cozdavatel()


    def cozdavatel(self):
        print(14567890)
        self.type = font.render(self.str_l+str(int(self.num))+self.str_r, True, [255, 255, 255])
    def paint(self):
        pygame.display.get_surface().blit(self.type, [self.x,self.y])

