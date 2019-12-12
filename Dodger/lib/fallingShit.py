import pygame
import random

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736


class FallingShit:

    def __init__(self):
        self.image = pygame.image.load("./pics/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = (random.randint(0, 40) * 32)
        self.rect.y = -32
        self.toBeRemoved = None

    def update(self):
        self.rect.y += 1

        if self.rect.y > WINDOW_HEIGHT:
            self.toBeRemoved = True

    def getRemovedStatus(self):
        return self.toBeRemoved

    def getRect(self):
        return self.rect

    def draw(self, surface):
        surface.blit(self.image, self.rect)
