import pygame

# Images #
iconImage = pygame.image.load('images/icon.png')
idleImage = pygame.image.load('images/character/Idle.png')

charImage = idleImage
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

mouse = pygame.mouse.get_pos() # track mouse X and Y position
mouseX = mouse[0]
mouseY = mouse[1]

playerRect = (32, 32)
xPos = 100
yPos = 100

animateNum = 0
sheetNum = 0

timer = 0
localFlashTimer = 0
menuFlash = False