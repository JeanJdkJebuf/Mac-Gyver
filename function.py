#import modules
import pygame

#create function to simplify code
def keypressed(touche, event):
    "function that returns true"
    return event.type == pygame.KEYDOWN and event.key == touche