import pygame, time
import view, model, control

while True:
    time.sleep(1 / 100)
    control.event_get()
    view.draw()

