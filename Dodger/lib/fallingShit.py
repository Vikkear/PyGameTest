import pygame
import random

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736


class FallingShit:

    def __init__(self):
        self.image = pygame.image.load("./pics/enemy.png")
        self.size = random.randint(18, 100)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = (random.randint(0, 40) * 32)
        self.rect.y = -32
        self.toBeRemoved = None

    def update(self):
        self.rect.y += 1
        saveX = self.rect.x
        saveY = self.rect.y

        self.size += 1
        #self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = saveX
        self.rect.y = saveY

        if self.rect.y > WINDOW_HEIGHT:
            self.toBeRemoved = True

    def getRemovedStatus(self):
        return self.toBeRemoved

    def getRect(self):
        return self.rect

    def draw(self, surface):
        surface.blit(self.image, self.rect)
