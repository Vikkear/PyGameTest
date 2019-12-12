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

        pygame.display.set_caption('Hello World!')

        self.player = Player() 
        self.enemy = FallingShit()        

        while True:

            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gameOver()

                    if event.key == pygame.K_UP:
                        self.player.moveUp()

                    if event.key == pygame.K_LEFT:
                        self.player.moveLeft()

                    if event.key == pygame.K_DOWN:
                        self.player.moveDown()

                    if event.key == pygame.K_RIGHT:
                        self.player.moveRight()

                if event.type == QUIT:
                    self.die()

            self.draw()
            self.enemy.update()
            pygame.display.update()
            time.sleep(50.0 / 1000.0)

    def draw(self):
        # The screen will be covered in black
        self.DISPLAYSURF.fill((0, 0, 0))
        # Draw player
        self.player.draw(self.DISPLAYSURF)
        # Draw Enemies
        self.enemy.draw(self.DISPLAYSURF)
        

    # Death to the game :>
    def die(self):
        pygame.quit()
        sys.exit()

    # TODO: Add logic
    def gameOver(self):
        self.die()


if __name__ == "__main__":
    theApp = App()
    theApp.main()
