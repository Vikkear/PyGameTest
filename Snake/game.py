import pygame
import sys
from pygame.locals import *
import time
from lib.apple import Apple
from lib.player import Player
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

        pygame.display.set_caption('Hello World!')
        self.playerImg = pygame.image.load('./pics/player.png')
        self.appleImg = pygame.image.load('./pics/apple.png')
        self.player = Player()
        self.apple = Apple()

        self.score = 0
        self.clock = pygame.time.Clock()

        # Text
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.text = self.font.render(
            'Score: ' + str(self.score), True, white, black)
        self.textRect = self.text.get_rect()
        self.textRect.x = 1200
        self.textRect.y = 700

        while True:

            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()

                    if event.key == pygame.K_UP:
                        self.player.moveUp()

                    if event.key == pygame.K_DOWN:
                        self.player.moveDown()

                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()

                    if event.key == pygame.K_ESCAPE:
                        self.die()

                if event.type == QUIT:
                    self.die()

            self.player.update()
            self.checkCollision()
            self.draw()
            pygame.display.update()
            time.sleep(50.0 / 1000.0)

    def draw(self):
        # The screen will be covered in black
        self.DISPLAYSURF.fill((0, 0, 0))
        # Draw our player
        self.player.draw(self.DISPLAYSURF)
        # Draw our apple
        self.apple.draw(self.DISPLAYSURF)
        # Draw our text
        self.DISPLAYSURF.blit(self.text, self.textRect)

    # Death to the game :>
    def die(self):
        pygame.quit()
        sys.exit()

    # TODO: Add logic
    def gameOver(self):
        self.die()


    def checkCollision(self):
        if self.player.isCollidingWithApple(self.apple.getRect()):
            self.score += 1
            self.text = self.font.render(
                'Score: ' + str(self.score), True, white, black)

            self.apple.respawn()

        if self.player.isCollidingWithMyself():
            self.gameOver()


if __name__ == "__main__":
    theApp = App()
    theApp.main()
