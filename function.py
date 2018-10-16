#import modules
import pygame

#create function to simplify code
def keypressed(touche, event):
    "function that returns true"
    return event.type == pygame.KEYDOWN and event.key == touche

def check_out(pos,wall) :
    "function checks if player out of bounds"
    #horizontally
    if pos[0]>=600 or pos[0]<0 :
        return True
    #vertically
    if pos[1]>= 600 or pos[1]<0 :
        return True
    #if new position is in wall
    if pos in wall :
        return True
    #otherwise return false
    else :
        return False
        
        