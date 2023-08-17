import pygame, model

def event_get():
    e=pygame.event.get()
    for event in e:
        if event.type==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("zqawsxedcrfvtgbyhnujmik,o")
