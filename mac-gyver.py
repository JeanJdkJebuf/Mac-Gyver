############################################################
#               Mac Gyver game
#       Game where we have to collect items to be able 
#                   to escape
############################################################
#               Script Python
#       Files : mac-gyver.py, classes.py, constant.py,
#       function.py, image_use, level.json
############################################################

############################################################
# import modules
############################################################ 

from constant import *
import classes
import pygame
import function

############################################################
# launching pygame
############################################################
pygame.init()

############################################################
# creating main window
############################################################

#dimension of main window, game window is a square
fen = pygame.display.set_mode((right_side,up_side))

# main windows' name
pygame.display.set_caption(fen_title)

############################################################
#instantiate class movement under var mc
mc=classes.movement(position=mcpos)

#adding character skin
char = pygame.image.load(mac_image).convert_alpha()

############################################################
#instantiate class level under var obj_lev
obj_lev=classes.level("level.json")
#creates a list to display it on screen ( later on )
obj_lev.create_a_list()

#this function adds solid objects character can't reach
mc.get_wall(obj_lev.list_wall())

############################################################
#creates items for level
items = classes.items(obj_lev.list_wall())
#knowing spawn, ending and walls position, creates place
#for items
items.create_pos()

############################################################
# main loop
############################################################
while continue_main :
    #change refresh @30 ms
    pygame.time.Clock().tick(30)

    #displays ground
    obj_lev.shows(fen)

    #lays items on the ground
    items.item_ground(fen)

    #stick mac gyver skin's new position on screen
    fen.blit(char,mcpos)

    #refreshing screen to update skin's position
    pygame.display.flip()

    #stops the game if the exit is reached
    if mcpos == mcstairs :
        continue_main = False
    #events to play or leave the game
    for event in pygame.event.get():
        #for events == keydown
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN or event.key== pygame.K_UP or event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT :
                #tuple that make mac gyver move
                tupmac=mc.move(event)
                mcpos=(tupmac[0],tupmac[1])
        #leave the game by pressing "q" or red cross, top right of screen
        if event.type == pygame.QUIT or function.keypressed(pygame.K_q , event):
            continue_main = False