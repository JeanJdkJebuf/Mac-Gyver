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
        #walls position
        #will fill it with get_wall function
        self.wall=[]

    def get_wall( self, liste ) :
        "use this function with a list to add solid objects character can't cross"
        for x in liste :
            self.wall.append(x)    

    def move(self, event) :
        "mac gyver's moves"
        #mac gyver goes down
        if function.keypressed(pygame.K_DOWN, event) :
            #do not add position if mac gyver is bottom screen
            if self.position[1]+40 >= 600 :
                return self.position
            #if mac gyver goes into a wall
            if  (self.position[0],self.position[1]+40) in self.wall :
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
            #if mac gyver goes into a wall 
            if  (self.position[0],self.position[1]-40) in self.wall :
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
            #if mac gyver goes into a wall
            if  (self.position[0]+40,self.position[1]) in self.wall :
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
            if  (self.position[0]-40,self.position[1]) in self.wall :
                return self.position
            #add -40 position[0] ( moves one square )
            else :
                self.position=(self.position[0]-40,self.position[1])
                return self.position

#class that generates level
class level(object) :
    "this class generates a level"
    def __init__(self, level) :
        #level that you create
        self.level=level
        self.liste=[]
    
    #this function returns a list from level.json file
    def create_a_list(self):
        with open(self.level) as f:
            data = json.load(f)
            self.liste=data.get("liste")
    
    #this function displays walls 
    def shows(self,window) :
        "this function displays walls"
        #pictures to paste
        mcwall1=pygame.image.load(wall1).convert()
        mcwall2=pygame.image.load(wall2).convert()
        mcback1=pygame.image.load(back1).convert()
        mcback2=pygame.image.load(back2).convert()
        way_out=pygame.image.load(exit).convert_alpha()
        for ligne in range(len(self.liste)) :
            #for each line in liste
            for car in range(len(self.liste[ligne])) :
                #for each caracter in line
                #adds walls
                if self.liste[ligne][car] == "m" :
                    window.blit(mcwall1,(car*40,ligne*40))
                if self.liste[ligne][car] == "n" :
                    window.blit(mcwall2,(car*40,ligne*40))
                #adds ground
                if self.liste[ligne][car] == "0" :
                    window.blit(mcback1,(car*40,ligne*40))
                if self.liste[ligne][car] == "1" :
                    window.blit(mcback2,(car*40,ligne*40))
                #adds exit at position defined
                #modify tuple to modify exit
                if self.liste[ligne][car] == "e" :
                    window.blit(way_out,(560,560))
    
    #this function returns walls tuple
    def list_wall(self):
        #local list = wally
        wally=[]
        #convert a list into a list of tuples
        for ligne in range(len(self.liste)) :
            for car in range(len(self.liste[ligne])) :
                #adds tags "m" and "n" ( both walls )
                if self.liste[ligne][car] == "m" :
                    wally.append((car*40,ligne*40))
                if self.liste[ligne][car] == "n" :
                    wally.append((car*40,ligne*40))
        return wally
    