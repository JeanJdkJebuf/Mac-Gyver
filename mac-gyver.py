############################################################
#               Mac Gyver game
#       Game where we have to collect items to be able 
#                   to escape
############################################################
#               Script Python
#       Files : mac-gyver.py, class.py, constant.py, n1.json
############################################################

############################################################
# import modules
############################################################ 

from constant import *
import classes
import pygame

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
# main loop
############################################################
while continue_main :
    #change refresh @30 ms
    pygame.time.Clock().tick(30)

    #events to play or leave the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type==pygame.KEYDOWN and event.key==pygame.K_q:
            continue_main = False