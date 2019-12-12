import pygame
import random

class FallingShit:

    def __init__(self):
        self.image = pygame.image.load("./pics/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = (random.randint(0, 40) * 32)
        self.rect.y = -32

    def update(self):
        self.rect.y += 8

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    