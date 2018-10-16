############################################################
#           Classes made for Mac Gyver's game
############################################################

import json
from constant import *
import pygame
import function
import random


#character class ( moving )
class Movement(object) :
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
        #mac gyver's different skins
        self.img_down=pygame.image.load(mc_down).convert_alpha()
        self.img_up=pygame.image.load(mc_up).convert_alpha()
        self.img_right=pygame.image.load(mc_right).convert_alpha()
        self.img_left=pygame.image.load(mc_left).convert_alpha()

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
            
            #if mac gyver goes into a wall
            if  function.check_out((self.position[0],self.position[1]+40),self.wall) :
                return self.position
            #add +40 ( moves one square )
            else :
                self.position=(self.position[0],self.position[1]+40)
                return self.position
        
        #mac gyver goes up
        if function.keypressed(pygame.K_UP, event) :
            #modifies where character looks
            self.look_at=2

            #if mac gyver goes into a wall 
            if  function.check_out((self.position[0],self.position[1]-40),self.wall) :
                return self.position
            #add -40 ( moves one square )
            else :
                self.position=(self.position[0],self.position[1]-40)
                return self.position

        #mac gyver goes right
        if function.keypressed(pygame.K_RIGHT, event) :
            #modifies where character looks
            self.look_at=3

            #if mac gyver goes into a wall
            if  function.check_out((self.position[0]+40,self.position[1]),self.wall) :
                return self.position
            #add +40 position[0] ( moves one square )
            else :
                self.position=(self.position[0]+40,self.position[1])
                return self.position
        
        #mac gyver goes left
        if function.keypressed(pygame.K_LEFT, event) :
            #modifies where character looks
            self.look_at=4

            if  function.check_out((self.position[0]-40,self.position[1]),self.wall) :
                return self.position
            #add -40 position[0] ( moves one square )
            else :
                self.position=(self.position[0]-40,self.position[1])
                return self.position
    
    def looking_at(self) :
        "This function gives a skin related to key pressed"
        #returns proper skin
        #list with all skins
        liste=[0,self.img_down,self.img_up,self.img_right,self.img_left]
        return liste[self.look_at]

#class that generates level
class Level(object) :
    "this class generates a level"
    def __init__(self, level) :
        #level that you create
        self.level=level
        self.liste=[]
        #pictures to paste
        self.mcwall1=pygame.image.load(wall1).convert()
        self.mcwall2=pygame.image.load(wall2).convert()
        self.mcback1=pygame.image.load(back1).convert()
        self.mcback2=pygame.image.load(back2).convert()
        self.way_out=pygame.image.load(exit).convert_alpha()
    
    #this function returns a list from level.json file
    def create_a_list(self):
        with open(self.level) as f:
            data = json.load(f)
            self.liste=data.get("liste")
    
    #this function displays walls 
    def shows(self,window) :
        "this function displays walls"
        for ligne in range(len(self.liste)) :
            #for each line in liste
            for car in range(len(self.liste[ligne])) :
                #for each caracter in line
                #adds walls
                if self.liste[ligne][car] == "m" :
                    window.blit(self.mcwall1,(car*40,ligne*40))
                if self.liste[ligne][car] == "n" :
                    window.blit(self.mcwall2,(car*40,ligne*40))
                #adds ground
                if self.liste[ligne][car] == "0" :
                    window.blit(self.mcback1,(car*40,ligne*40))
                if self.liste[ligne][car] == "1" :
                    window.blit(self.mcback2,(car*40,ligne*40))
                #adds exit at position defined
                #modify tuple to modify exit
                if self.liste[ligne][car] == "e" :
                    window.blit(self.way_out,(560,560))
    
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
class Items(object) :
    "this class creates items and places them randomly"
    def __init__(self,level):
        #level is a list of tuples that shows where walls are
        self.level=level
        #list of tuple of items position
        self.item_list=[]
        #win condition
        self.win_cond=[(40,600),(120,600),(200,600)]
        #creates items skin
        self.mcneedle=pygame.image.load(needle).convert_alpha()
        self.mcether=pygame.image.load(ether).convert_alpha()
        self.mcplastic=pygame.image.load(plastic).convert_alpha()
    
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
        
        #moving items if mcGyver walks on it
        for x in range(len(self.item_list)) :
            if pos == self.item_list[x]:
                #adding win condition
                self.item_list[x]=self.win_cond[x]

        #copies items on the ground
        window.blit(self.mcneedle,self.item_list[0])
        window.blit(self.mcether,self.item_list[1])
        window.blit(self.mcplastic,self.item_list[2])
    
    def win_func(self) :
        "this function returns True if mac gyver took all items"
        all_items=True
        for x in range(len(self.item_list)) :
            #if mc doens't walked on items
            if self.item_list[x] != self.win_cond[x] :
                all_items = False
        
        return all_items
            