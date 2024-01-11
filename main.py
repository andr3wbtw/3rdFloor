import pygame
import os
from pygame.locals import*

import menu
import game
import variables

def main():
    ### MAIN GAME LOOP ###
    while True:
        ev = pygame.event.poll()    # Look for any even

        object_list = pygame.sprite.Group() # Object list
        
        variables.mouse = pygame.mouse.get_pos() # track mouse X and Y position
        variables.mouseX = variables.mouse[0]
        variables.mouseY = variables.mouse[1]

        if(variables.goingUp == True):
            variables.yPos -= 0.4
            variables.charImage = variables.runImage
            variables.sheetNum = 128
        elif(variables.goingDown == True):
            variables.yPos += 0.4
            variables.charImage = variables.runImage
            variables.sheetNum = 0
        elif(variables.goingRight == True):
            variables.xPos += 0.4
            variables.charImage = variables.runImage
            variables.sheetNum = 256
        elif(variables.goingLeft == True):
            variables.xPos -= 0.4
            variables.charImage = variables.runImage
            variables.sheetNum = 384
        else:
            variables.charImage = variables.idleImage
            variables.sheetNum = 0

        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w:
                variables.goingUp = True
            elif ev.key == pygame.K_s:
                variables.goingDown = True
            elif ev.key == pygame.K_d:
                variables.goingRight = True
            elif ev.key == pygame.K_a:
                variables.goingLeft = True
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_w:
                variables.goingUp = False; variables.animateNum = 0
            elif ev.key == pygame.K_s: 
                variables.goingDown = False; variables.animateNum = 0
            elif ev.key == pygame.K_d:
                variables.goingRight = False; variables.animateNum = 0
            elif ev.key == pygame.K_a:
                variables.goingLeft = False; 
            
        if variables.gameState == "menu": # menu state
            menu.menu()
            if ev.type == pygame.MOUSEBUTTONUP:
                variables.gameState = "game"
        pygame.display.flip()
        if variables.gameState == "game":
            game.game()
            variables.screen.blit(variables.charImage, (variables.screenX/2 - 96, variables.screenY/2 - 96), (variables.animateNum, variables.sheetNum, 128, 128)) # 32 is the sprite size
            if(variables.timer % 100 == 0):
                if((variables.goingUp == False) and (variables.goingDown == False) and (variables.goingRight == False) and (variables.goingLeft == False)):
                    if(variables.animateNum == 0):
                        variables.animateNum = 128
                    else:
                        variables.animateNum = 0
                elif((variables.goingUp == True) or (variables.goingDown == True) or (variables.goingRight == True) or (variables.goingLeft == True)):
                    if(variables.animateNum == 0):
                        variables.animateNum = 128
                    elif(variables.animateNum == 128):
                        variables.animateNum = 256
                    elif(variables.animateNum == 256):
                        variables.animateNum = 384
                    else:
                        variables.animateNum = 0
        variables.timer+= 1 # tick the timer

        pygame.display.flip()
    pygame.quit()

main()
