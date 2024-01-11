import pygame
import variables

menuImage = pygame.image.load('images/menuscreen.png')

trees = []

class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, filename):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = pygame.image.load(filename).convert()

class Tree(pygame.sprite.Sprite):
    def __init__(self, dx, dy, filename):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = dx
        self.rect.y = dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)


trees.append(Tree(100, 100, 'images/Tree.png'))

#tree1 = Tree(200, 200, 'images/Tree.png')

def game():
    variables.screen.fill((35, 99, 52))
    for Tree in trees:
        Tree.draw(variables.screen)
    #tree1.draw(variables.screen)
        
print(trees)