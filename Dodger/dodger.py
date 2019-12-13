import pygame
import sys
from pygame.locals import *
import time
from lib.player import Player
from lib.fallingShit import FallingShit

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 128)


class App:

    def main(self):
        pygame.init()

        self.DISPLAYSURF = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT))

        pygame.display.set_caption('Dodger v0.1')

        self.mainmenuImg = pygame.image.load("./pics/mainmenu.png")
        self.arrowImg = pygame.image.load("./pics/arrow.png")

        self.gameState = "MENU"
        self.timer = 0
        self.currentChoice = 0
        self.gameOverFlag = 0

        # Text
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.gameOverFont = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(
            'Tid: ' + str(self.timer), True, white, black)
        self.textRect = self.text.get_rect()
        self.textRect.x = 1200
        self.textRect.y = 700

        # Arrow
        self.arrowRect = self.arrowImg.get_rect()
        self.arrowRect.x = 700
        self.arrowRect.y = 125
        while True:

            if self.gameState == "MENU":
                self.DISPLAYSURF.blit(self.mainmenuImg, (0, 0))
                self.DISPLAYSURF.blit(self.arrowImg, self.arrowRect)
                self.menuKeys()

            if self.gameState == "GAME":
                self.keyChecks()
                self.draw()
                self.update()

            if self.gameState == "GAMEOVER":
                self.gameOverMenu()
                self.menuKeys()

            pygame.display.update()
            time.sleep(5.0 / 1000.0)

    def menuKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.gameOverFlag == 0:
                    self.handleEnterInMenu()

                if event.key == pygame.K_RETURN and self.gameOverFlag == 1:
                    self.gameState = "MENU"
                    self.gameOverFlag = 0

                if event.key == pygame.K_ESCAPE:
                    self.die()

                if event.key == pygame.K_DOWN and self.currentChoice < 3:
                    self.arrowRect.y += 125
                    self.currentChoice += 1

                if event.key == pygame.K_UP and self.currentChoice > 0:
                    self.arrowRect.y -= 125
                    self.currentChoice -= 1

            if event.type == QUIT:
                self.die()

    def handleEnterInMenu(self):
        if self.currentChoice == 0:
            self.startGame()

        elif self.currentChoice == 3:
            self.die()

        else:
            print("Not implemented u piece of garbage")

    def startGame(self):
        self.player = Player()
        self.enemies = []
        self.amountOfEnemies = 0
        self.spawnEnemy()
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.enemyTimer = 0
        self.timeUntilEnemySpawns = 2000
        self.gameState = "GAME"

    def gameOverMenu(self):
        self.DISPLAYSURF.fill((0, 0, 0))
        self.gameOverText = self.gameOverFont.render(
            'Score: ' + str(int(self.timer/1000)), True, white, black)
        self.gameOverTextRect = self.gameOverText.get_rect()
        self.gameOverTextRect.x = 600
        self.gameOverTextRect.y = 300

        self.gameOverReturn = self.gameOverFont.render(
            'Press Return to go back to the Main Menu!', True, white, black)
        self.gameOverReturnRect = self.gameOverText.get_rect()
        self.gameOverReturnRect.x = 320
        self.gameOverReturnRect.y = 360

        self.DISPLAYSURF.blit(self.gameOverText, self.gameOverTextRect)
        self.DISPLAYSURF.blit(self.gameOverReturn, self.gameOverReturnRect)

        # Creates new enemy and add it to the enemy array

    def spawnEnemy(self):
        enemy = FallingShit()
        self.enemies.append(enemy)
        self.amountOfEnemies += 1

    # Contains game logic
    def update(self):

        # Time keeper
        self.clock.tick()
        self.timer += self.clock.get_time()
        self.enemyTimer += self.clock.get_time()

        self.text = self.font.render(
            'Tid: ' + str(int(self.timer/1000)), True, white, black)

        if self.enemyTimer > self.timeUntilEnemySpawns:
            self.enemyTimer = 0
            self.spawnEnemy()

        if self.timer > 10000:
            self.timeUntilEnemySpawns = 500

        self.checkCollision()

        for i in range(0, self.amountOfEnemies):
            self.enemies[i].update()
            if self.enemies[i].getRemovedStatus():
                enemyToRemove = self.enemies.pop(i)
                del enemyToRemove
                self.amountOfEnemies -= 1
                break

        # Contains logic for key presses
    def keyChecks(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.player.moveUp()
        if keys[pygame.K_DOWN]:
            self.player.moveDown()
        if keys[pygame.K_LEFT]:
            self.player.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.player.moveRight()

        # Event Handler
        for event in pygame.event.get():
            if event.type == QUIT:
                self.die()

    # Draws everything onto the screen
    def draw(self):
        # The screen will be covered in black
        self.DISPLAYSURF.fill((0, 0, 0))
        # Draw player
        self.player.draw(self.DISPLAYSURF)
        # Draw Enemies
        for i in range(0, self.amountOfEnemies):
            self.enemies[i].draw(self.DISPLAYSURF)
        # Draw our text
        self.DISPLAYSURF.blit(self.text, self.textRect)

    # Death to the game :>
    def die(self):
        pygame.quit()
        sys.exit()

    # TODO: Add logic
    def gameOver(self):
        self.gameOverFlag = 1
        self.gameState = "GAMEOVER"
        self.currentChoice = 0
        self.arrowRect.x = 700
        self.arrowRect.y = 125

    # Contains collision logic

    def checkCollision(self):
        for i in range(0, self.amountOfEnemies):
            if self.player.isCollidingWith(self.enemies[i].getRect()):
                self.gameOver()


if __name__ == "__main__":
    theApp = App()
    theApp.main()
