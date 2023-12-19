import pygame
from pygame.locals import*

import menu
from variables import *

def main():
    ### MAIN GAME LOOP ###
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        if gameState == "menu": # menu state
            menu.menu()
        pygame.display.flip()
    pygame.quit()

main()
