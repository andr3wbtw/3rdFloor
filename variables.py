import pygame

# Images #
iconImage = pygame.image.load('images/icon.png')
# # # # # # # # # # # # # # # # # # # # # # # # #
# Essentials #
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()  #Force frame rate to be slower
pygame.display.set_caption('3rd Floor') # change window name
pygame.display.set_icon(iconImage) # change window icon
gameState = "menu"
# # # # # # # # # # # # # # # # # # # # # # # # #

info = pygame.display.Info()
w = info.current_w
h = info.current_h

screenX = 1280
screenY = 680
screen = pygame.display.set_mode((screenX, screenY))
