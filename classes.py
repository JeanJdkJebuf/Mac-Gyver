############################################################
#           Classes made for Mac Gyver's game
############################################################

import json
from constant import *
import pygame
import function
import random


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
        #this var allows different skins for mac gyver
        self.look_at=3

    def get_wall( self, liste ) :
        "use this function with a list to add solid objects character can't cross"
        for x in liste :
            self.wall.append(x)    

    def move(self, event) :
        "mac gyver's moves"
        #mac gyver goes down
        if function.keypressed(pygame.K_DOWN, event) :
            #modifies where character looks
            self.look_at=1
            
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
            #modifies where character looks
            self.look_at=2

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
            #modifies where character looks
            self.look_at=3

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
            #modifies where character looks
            self.look_at=4

            #do not add position if pos[0] == 0 ( means he is left)
            if self.position[0] == 0 :
                return self.position
            if  (self.position[0]-40,self.position[1]) in self.wall :
                return self.position
            #add -40 position[0] ( moves one square )
            else :
                self.position=(self.position[0]-40,self.position[1])
                return self.position
    
    def looking_at(self) :
        "This function gives a skin related to key pressed"
        #
        img_down=pygame.image.load(mc_down).convert_alpha()
        img_up=pygame.image.load(mc_up).convert_alpha()
        img_right=pygame.image.load(mc_right).convert_alpha()
        img_left=pygame.image.load(mc_left).convert_alpha()
        #list with all skins
        liste=[0,img_down,img_up,img_right,img_left]
        #returns proper skin
        return liste[self.look_at]

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

#For lisibility, i'm going to create this class
#I could implemente it to movement class,
#but it would make that class hard to read
class items(object) :
    "this class creates items and places them randomly"
    def __init__(self,level):
        #level is a list of tuples that shows where walls are
        self.level=level
        #list of tuple of items position
        self.item_list=[]
        #win condition
        self.win_cond=[(120,600),(160,600),(200,600)]
    
    def create_pos(self) :
        "this function creates position for items among the map"
        #while items position aren't avalaible yet
        while len(self.item_list)<3 :
            test=(random.randrange(15)*40,random.randrange(15)*40)
            if test in self.level or test ==mcpos or test == mcstairs or test in self.item_list :
                continue
            else :
                self.item_list.append(test)

    def item_ground(self,window, pos) :
        "this function lays items on the ground"
        #creates items skin
        mcneedle=pygame.image.load(needle).convert_alpha()
        mcether=pygame.image.load(ether).convert_alpha()
        mcplastic=pygame.image.load(plastic).convert_alpha()
        
        #moving items if mcGyver walks on it
        for x in range(len(self.item_list)) :
            if pos == self.item_list[x]:
                #adding win condition
                self.item_list[x]=self.win_cond[x]

        #copies items on the ground
        window.blit(mcneedle,self.item_list[0])
        window.blit(mcether,self.item_list[1])
        window.blit(mcplastic,self.item_list[2])
    
    def win_func(self) :
        "this function returns True if mac gyver took all items"
        all_items=True
        for x in range(len(self.item_list)) :
            #if mc doens't walked on items
            if self.item_list[x] != self.win_cond[x] :
                all_items = False
        
        return all_items
            