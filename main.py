# Following the tutorial by dr0id.bitbucket.io

# import the pygame module, so you can use it
import pygame

# define a main function


def main():
    clock = pygame.time.Clock()
    clock.tick(1000)
    screen_width = 1600
    screen_height = 900

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Oni 2")

    # create a surface on screen that has the size of 1600 x 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((170, 200, 255))

    # Images
    image = pygame.image.load("01_image.png")
    image.set_colorkey((255, 0, 255))
    screen.blit(image, (50, 50))
    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # define the position of the smiley
    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 10
    step_y = 10

    # main loop
    while running:
        # check if the smiley is still on screen, if not change direction
        if xpos > screen_width-64 or xpos < 0:
            step_x = -step_x
        if ypos > screen_height-64 or ypos < 0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x  # move it to the right
        ypos += step_y  # move it down

        # first erase the screen
        # (just blit the background over anything on screen)
        screen.fill((170, 200, 255))
        # now blit the smiley on screen
        screen.blit(image, (xpos, ypos))
        # and update the screen (don't forget that!)
        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
