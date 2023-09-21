import pygame

pygame.init()
font = pygame.font.SysFont('comicsansms', 25)


class Writer:
    def __init__(self, str_l, str_r, x, y, num=0, color=[255, 255, 255]):
        self.str_l = str_l
        self.str_r = str_r
        self.x = x
        self.y = y
        self.num = num
        self.color = color
        self.cozdavatel()

    def cozdavatel(self):
        # print(14567890)
        self.type = font.render(self.str_l + str(int(self.num)) + self.str_r, True, self.color)

    def paint(self):
        pygame.display.get_surface().blit(self.type, [self.x, self.y])

    @property
    def my_color(self):
        if self.color == [255, 255, 255]:
            b = 'белый'
        elif self.color == [0, 0, 255]:
            b = 'blue'
        else:
            b = 'другой цвет'
        return b

    @my_color.setter
    def my_color(self, where_you):
        if where_you == 'blue':
            self.color = [0, 0, 255]
        elif where_you == 'white':
            self.color = [255, 255, 255]

    @property
    def number(self):
        return self.num

    @number.setter
    def number(self, rgb):
        if rgb != self.num:
            self.num = rgb
            self.cozdavatel()
