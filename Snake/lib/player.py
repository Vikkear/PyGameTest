import pygame
import math
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736

class Player:
    # Direction: 0 = right, 1 = down, 2 = left, 3 = up
    def __init__(self):
        self.image = pygame.image.load('./pics/player.png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0
        self.length = 1
        self.xPos = [0]
        self.yPos = [0]
        self.speed = 32
        self.direction = 0

    def moveLeft(self):
        if self.direction != 0:
            self.direction = 2

    def moveUp(self):
        if self.direction != 1:
            self.direction = 3

    def moveRight(self):
        if self.direction != 2:
            self.direction = 0

    def moveDown(self):
        if self.direction != 3:
            self.direction = 1

    def getPosition(self, type):
        if type == "X":
            returnValue = self.rect.x
        else:
            returnValue = self.rect.y
        return returnValue

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

        if self.rect.x > WINDOW_WIDTH-32:
            self.rect.x = 0
        
        if self.rect.x < 0:
            self.rect.x = WINDOW_WIDTH

        if self.rect.y > WINDOW_HEIGHT-32:
            self.rect.y = 0

        if self.rect.y < 0:
            self.rect.y = WINDOW_HEIGHT

        # Position Logic
        if self.length >= 2:
            for i in range(self.length-1, 0, -1):
                self.xPos[i] = self.xPos[i-1]
                self.yPos[i] = self.yPos[i-1]

        self.xPos[0] = self.rect.x
        self.yPos[0] = self.rect.y

       

    def draw(self, surface):
        # Draw Head
        surface.blit(
            self.image, self.rect)

        for i in range(0, self.length-1):
            surface.blit(self.image, (self.xPos[i], self.yPos[i]))

    def updateLength(self):
        self.xPos.append(self.xPos[self.length-1])
        self.yPos.append(self.yPos[self.length-1])
        self.length += 1

    def isCollidingWithApple(self, apple):
        isColliding = None

        if self.rect.colliderect(apple):
            isColliding = True
            self.updateLength()
            

        return isColliding

    def isCollidingWithMyself(self):
        isColliding = None

        for i in range(1, self.length-1, 1):
            if math.sqrt((self.xPos[i]-self.xPos[0])**2 +  (self.yPos[i] - self.yPos[0])**2) < 32:
                isColliding = True

        return isColliding
