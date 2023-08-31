import pygame

pygame.init()
font = pygame.font.SysFont('comicsansms', 25)


class Writer:
    def __init__(self, str, x, y):
        self.str = str
        self.x = x
        self.y = y
        print(1)

    def cozdavatel(self):
        self.type = font.render(str(self.str), True, [255, 255, 255])
        pygame.display.get_surface().blit(self.type, [self.x,self.y])

