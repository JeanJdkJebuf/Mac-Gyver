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

#You can keep one button pressed to move faster
pygame.key.set_repeat(400,30)

############################################################
#instantiate class movement under var mc
mc=classes.Movement(position=mcpos)

############################################################
#instantiate class level under var obj_lev
obj_lev=classes.Level("level.json")
#creates a list to display it on screen ( later on )
obj_lev.create_a_list()

#this function adds solid objects character can't reach
mc.get_wall(obj_lev.list_wall())

############################################################
#creates items for level
items = classes.Items(obj_lev.list_wall())
#knowing spawn, ending and walls position, creates place
#for items
items.create_pos()

############################################################
#Adding level design
############################################################
#item spacebar
item_spacebar=pygame.image.load(item_bar).convert()
#bad ending
bad_ending=pygame.image.load(bd_ending).convert()
#good ending
good_ending=pygame.image.load(gd_ending).convert()

############################################################
# main loop
############################################################
while continue_main :
    #change refresh @30 ms
    pygame.time.Clock().tick(30)

    #displays ground
    obj_lev.shows(fen)

    #items spacebar
    fen.blit(item_spacebar,loc_item_bar)

    #lays items on the ground
    items.item_ground(fen, mcpos)

    #stick mac gyver skin's new position on screen
    fen.blit(mc.looking_at(),mcpos)

    #refreshing screen to update skin's position
    pygame.display.flip()

    #bad ending
    if mcpos == mcstairs and items.win_func()==False :
        #displays bad ending screen
        fen.blit(bad_ending,ending)
        #refresh screen
        pygame.display.flip()
        #for 3000 ms
        pygame.time.wait(4000)
        #then stops loop
        continue_main = False
    
    #stops the game if mac gyver got all items
    if mcpos == mcstairs and items.win_func() :
        #displays good ending screen
        fen.blit(good_ending,ending)
        #refresh screen
        pygame.display.flip()
        #for 3000 ms
        pygame.time.wait(4000)
        #then stops loop
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