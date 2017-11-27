import pygame

class Block(pygame.sprite.DirtySprite):
    def __init__(self, x, y):
        pygame.sprite.DirtySprite.__init__(self)
        self.dirty = 1

        self.image = pygame.image.load('../assets/grass.png').convert()
        self.rect = pygame.Rect(x, y, 50, 50)
    
#BITCHAZZZZ