import pygame
pygame.font.init()
import variables

menuImage = pygame.image.load('images/menuscreen.png')
lucidityFont = pygame.font.Font('fonts/lucidityfont.otf',50)
lucidityFontOutline = pygame.font.Font('fonts/lucidityfont.otf',52)

clickToPlay = lucidityFont.render("CLICK TO PLAY", True, (218,176,51))
clickToPlay_rect = clickToPlay.get_rect(center=(variables.screenX/2, variables.screenY/2))

clickToPlayOutline = lucidityFontOutline.render("CLICK TO PLAY", True, (0, 0, 0))
clickToPlayOutline_rect = clickToPlayOutline.get_rect(center=(variables.screenX/2, variables.screenY/2))

def menu():
    variables.screen.blit(menuImage, (0,0))

    if((variables.timer % 80) == 0):
        variables.menuFlash = True
        
    if(variables.menuFlash == True):
        if(variables.localFlashTimer < 80):
            variables.screen.blit(clickToPlayOutline, (clickToPlayOutline_rect[0], 498))
            variables.screen.blit(clickToPlay, (clickToPlay_rect[0], 500))
            variables.localFlashTimer+= 1
        elif(variables.localFlashTimer >= 80):
            variables.localFlashTimer = 0
            variables.menuFlash = False