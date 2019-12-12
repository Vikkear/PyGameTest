import pygame


class Player:
    # Direction: 0 = right, 1 = down, 2 = left, 3 = up
    def __init__(self):
        self.image = pygame.image.load('./pics/player.png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0
        self.speed = 32
        self.direction = 0

    def moveLeft(self):
        self.direction = 2

    def moveUp(self):
        self.direction = 3

    def moveRight(self):
        self.direction = 0

    def moveDown(self):
        self.direction = 1

    def getPosition(self, type):
        if type == "X":
            returnValue = self.rect.x
        else:
            returnValue = self.rect.y
        return returnValue

    def getRect(self):
        return self.rect

    def update(self):
        # Movement
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y += self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        else:
            self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(
            self.image, self.rect)
