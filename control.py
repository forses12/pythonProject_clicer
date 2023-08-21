import pygame, model

def event_get():
    e=pygame.event.get()
    for event in e:
        if event.type==pygame.QUIT:
            exit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN :
            model.get_coin()
            print(model.coin)

