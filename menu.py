import pygame
from variables import *

menuImage = pygame.image.load('images/menuscreen.png')

def menu():
    screen.blit(menuImage, (0,0))
