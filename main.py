# this is an implementation of the A* algorithm

import pygame
import sys

# window dimentions
dis = (800,600)
root = pygame.display.set_mode(dis)

clock = pygame.time.Clock()
FPS = 60

def main(args):

    running = True

    while running:


        # exit game loop if quit or escape key if pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # clear window
        root.fill((255,255,255))

        #update window
        pygame.display.update()
        # wait until next frame
        clock.tick(FPS)



# error handling
if __name__ == '__main__':
    try:
        main(sys.argv)
    except Exception as e:
        # if an error occurs, quit pygame, then raise the error
        pygame.quit()
        raise e

    # after main, quit pygame and exit the program
    pygame.quit()
    sys.exit()