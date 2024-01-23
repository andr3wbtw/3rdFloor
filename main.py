import pygame
import os
import random
from pygame.locals import*

import menu
import variables

trees = []

class Tree(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.awayX = dx
        self.awayY = dy
        self.rect.x = variables.enviroPosX+self.awayX
        self.rect.y = variables.enviroPosY+self.awayY

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        self.rect.x = variables.enviroPosX+self.awayX
        self.rect.y = variables.enviroPosY+self.awayY

def generateTrees():
    for i in range(0, 50, 1):
        randX = random.randint(0,2900)
        randY = random.randint(0,1800)
        randTree = random.randint(1,3)
        if(randTree == 1):
            trees.append(Tree(randX, randY, 'images/Tree.png'))
        elif(randTree == 2):
            trees.append(Tree(randX, randY, 'images/Tree2.png'))
        elif(randTree == 3):
            trees.append(Tree(randX, randY, 'images/Tree3.png'))

def main():
    ### MAIN GAME LOOP ###
    while True:
        ev = pygame.event.poll()    # Look for any even

        object_list = pygame.sprite.Group() # Object list
        
        variables.mouse = pygame.mouse.get_pos() # track mouse X and Y position
        variables.mouseX = variables.mouse[0]
        variables.mouseY = variables.mouse[1]

        if((variables.goingUp == True) and (variables.enviroPosY < 345)):
            variables.enviroPosY += 0.6
            variables.charImage = variables.runImage
            variables.sheetNum = 128
        elif((variables.goingDown == True) and (variables.enviroPosY > -1625)):
            variables.enviroPosY -= 0.6
            variables.charImage = variables.runImage
            variables.sheetNum = 0
        elif((variables.goingRight == True) and (variables.enviroPosX > -2350)):
            variables.enviroPosX -= 0.6
            variables.charImage = variables.runImage
            variables.sheetNum = 256
        elif((variables.goingLeft == True) and (variables.enviroPosX < 570)):
            variables.enviroPosX += 0.6
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
            elif (ev.key == pygame.K_a) and (variables.enviroPosX < 570):
                variables.goingLeft = True
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_w:
                variables.goingUp = False; variables.animateNum = 0
            elif ev.key == pygame.K_s: 
                variables.goingDown = False; variables.animateNum = 0
            elif ev.key == pygame.K_d:
                variables.goingRight = False; variables.animateNum = 0
            elif ev.key == pygame.K_a:
                variables.goingLeft = False; variables.animateNum = 0
            
        if variables.gameState == "menu": # menu state
            menu.menu()
            if ev.type == pygame.MOUSEBUTTONUP:
                variables.gameState = "game"
                generateTrees()
        pygame.display.flip()
        if variables.gameState == "game":
            variables.screen.fill((0, 0, 0))
            ground = pygame.draw.rect(variables.screen, (35, 99, 52), pygame.Rect(variables.enviroPosX, variables.enviroPosY, 3000, 2000))
            variables.screen.blit(variables.charImage, (variables.screenX/2 - 96, variables.screenY/2 - 96), (variables.animateNum, variables.sheetNum, 128, 128)) # 32 is the sprite size
            for Tree in trees:
                Tree.draw(variables.screen)
                Tree.update()
            variables.darkScreen.set_alpha(160)
            variables.lightScreen.blit(variables.lightImage, (variables.screenX/2 - 210, variables.screenY/2 - 200))
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
        print(variables.enviroPosX, variables.enviroPosY)

        pygame.display.flip()
    pygame.quit()

main()
