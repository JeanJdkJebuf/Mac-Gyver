############################################################
#           Classes made for Mac Gyver's game
############################################################

import json
from constant import *
import pygame
import function


#character class ( moving )
class movement(object) :
    "this class allows mac gyver to move"
    def __init__(self,position=(0,0)) :
        "class strings"
        #character position
        self.position=position

    def move(self, event) :
        "mac gyver's moves"
        #mac gyver goes down
        if function.keypressed(pygame.K_DOWN, event) :
            #do not add position if mac gyver is bottom screen
            if self.position[1]+40 >= 600 :
                return self.position
            #add +40 ( moves one square )
            else :
                self.position=(self.position[0],self.position[1]+40)
                return self.position
        
        #mac gyver goes up
        if function.keypressed(pygame.K_UP, event) :
            #do not add position if mac gyver is top screen
            if self.position[1]-40<0 :
                return self.position
            #add -40 ( moves one square )
            else :
                self.position=(self.position[0],self.position[1]-40)
                return self.position

        #mac gyver goes right
        if function.keypressed(pygame.K_RIGHT, event) :
            #do not add position if mac gyver is top right
            if self.position[0]+40>=600 :
                return self.position
            #add +40 position[0] ( moves one square )
            else :
                self.position=(self.position[0]+40,self.position[1])
                return self.position
        
        #mac gyver goes left
        if function.keypressed(pygame.K_LEFT, event) :
            #do not add position if pos[0] == 0 ( means he is left)
            if self.position[0] == 0 :
                return self.position
            #add -40 position[0] ( moves one square )
            else :
                self.position=(self.position[0]-40,self.position[1])
                return self.position