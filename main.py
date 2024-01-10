import pygame
import os
from pygame.locals import*

import menu
import floor1
import variables

def moveUp():
    variables.yPos -= 2

def moveDown():
    variables.yPos += 2

def moveRight():
    variables.xPos += 2

def moveLeft():
    variables.xPos -= 2

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
        elif(variables.goingDown == True):
            variables.yPos += 0.4
            variables.charImage = variables.runImage
        elif(variables.goingRight == True):
            variables.xPos += 0.4
            variables.charImage = variables.runImage
        elif(variables.goingLeft == True):
            variables.xPos -= 0.4
            variables.charImage = variables.runImage
        else:
            variables.charImage = variables.idleImage

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
                variables.goingUp = False
            elif ev.key == pygame.K_s:
                variables.goingDown = False
            elif ev.key == pygame.K_d:
                variables.goingRight = False
            elif ev.key == pygame.K_a:
                variables.goingLeft = False
            
        if variables.gameState == "menu": # menu state
            menu.menu()
            if ev.type == pygame.MOUSEBUTTONUP:
                variables.gameState = "floor1"
        pygame.display.flip()
        if variables.gameState == "floor1":
            floor1.floor1()
            variables.screen.blit(variables.charImage, (variables.screenX/2 - 96, variables.screenY/2 - 96), (variables.animateNum, variables.sheetNum, 128, 128)) # 32 is the sprite size
            if(variables.timer % 300 == 0):
                if((variables.goingUp == False) and (variables.goingDown == False) and (variables.goingRight == False) and (variables.goingLeft == False)):
                    if(variables.animateNum == 0):
                        variables.animateNum = 128
                    else:
                        variables.animateNum = 0
                elif(variables.goingUp == True):
                    if(variables.animateNum == 0):
                        variables.animateNum = 32
                    elif(variables.animateNum == 32):
                        variables.animateNum = 64
                    elif(variables.animateNum == 64):
                        variables.animateNum = 96
                    else:
                        variables.animateNum = 0
        variables.timer+= 1 # tick the timer

        pygame.display.flip()
    pygame.quit()

main()
