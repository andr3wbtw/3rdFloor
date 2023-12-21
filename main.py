import pygame
import os
from pygame.locals import*

import menu
import floor1
import variables

def main():
    ### MAIN GAME LOOP ###
    while True:
        ev = pygame.event.poll()    # Look for any even

        object_list = pygame.sprite.Group() # Object list
        
        variables.mouse = pygame.mouse.get_pos() # track mouse X and Y position
        variables.mouseX = variables.mouse[0]
        variables.mouseY = variables.mouse[1]

        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if variables.gameState == "menu": # menu state
            menu.menu()
            if ev.type == pygame.MOUSEBUTTONUP:
                variables.gameState = "floor1"
        pygame.display.flip()
        if variables.gameState == "floor1":
            floor1.floor1()
            variables.screen.blit(variables.charImage, (variables.xPos, variables.yPos), (variables.animateNum, variables.sheetNum, 32, 32)) # 32 is the sprite size
            if(variables.timer % 300 == 0):
                if(variables.animateNum == 0):
                    variables.animateNum = 32
                else:
                    variables.animateNum = 0
        variables.timer+= 1 # tick the timer

        pygame.display.flip()
    pygame.quit()

main()
