import pygame
import random


class Apple:
    def __init__(self):
        # Ändra här för att aligna blocksen
        self.image = pygame.image.load('./pics/apple.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 22)
        self.rect.y = random.randint(0, 22)
        self.step = 32
        self.rect.x *= self.step
        self.rect.y *= self.step

    def getPosition(self, type):
        if type == "X":
            returnValue = self.rect.x
        else:
            returnValue = self.rect.y
        return returnValue

    def draw(self, surface):
        surface.blit(
            self.image, self.rect)

    def isCollidingWithPlayer(self, player):
        isColliding = None

        if self.rect.colliderect(player):
            isColliding = True

        return isColliding

    def respawn(self):
        self.rect.x = random.randint(0, 22)
        self.rect.y = random.randint(0, 22)
        self.step = 32
        self.rect.x *= self.step
        self.rect.y *= self.step
