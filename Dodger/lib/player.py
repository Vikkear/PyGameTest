import pygame
import random


class Player:
    def __init__(self):
        self.alive = True
        self.speed = 8
        self.image = pygame.image.load("./pics/player.png")
        self.rect = self.image.get_rect()
        self.x = random.randint(0, 22)
        self.y = random.randint(0, 20)
        self.rect.x = self.x * 32
        self.rect.y = self.y * 32

    def moveRight(self):
        self.rect.x += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed

    def moveUp(self):
        self.rect.y -= self.speed
    
    def moveDown(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

