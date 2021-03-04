# this is an implementation of the A* algorithm

import pygame
import sys
from random import randint

# pygame init -------------------------------------------------------------------------------------
# window dimentions
dis = (800,600)
root = pygame.display.set_mode(dis)

clock = pygame.time.Clock()
FPS = 60

# colours (english is best) -----------------------------------------------------------------------

bgColour = (255,255,255)
gridColour = (0,0,0)

startColour = (0,255,0)
endColour = (255,0,0)
wallColour = (200,200,200)

# grid setup --------------------------------------------------------------------------------------

cellWH = 10
noRows = dis[1]//cellWH
noCols = dis[0]//cellWH
# make sure there arn't any half cells outside the window
assert dis[0]%cellWH == 0 and dis[1]%cellWH == 0

# make the grid
grid = [[0 for i in range(noCols)] for i in range(noRows)]

# assign the start square a random position
start = [randint(0,noCols-1),randint(0,noRows-1)]

# assign the end square a random position that isn't the start square
end = [randint(0,noCols-1),randint(0,noRows-1)]
while end == start:
    end = [randint(0,noCols),randint(0,noRows)]

def drawGrid():
    # if you don't know what this does, um, learn pygame

    pygame.draw.rect(root,startColour,((start[0]*cellWH,start[1]*cellWH),(cellWH,cellWH)))
    pygame.draw.rect(root,endColour,((end[0]*cellWH,end[1]*cellWH),(cellWH,cellWH)))

    for y,row in enumerate(grid):
        for x,val in enumerate(row):
            if val:
                pygame.draw.rect(root,wallColour,(x*cellWH,y*cellWH,cellWH,cellWH))

    for i in range(noRows):
        pygame.draw.line(root,gridColour,(0,i*cellWH),(dis[0],i*cellWH),1)

    for i in range(noCols):
        pygame.draw.line(root,gridColour,(i*cellWH,0),(i*cellWH,dis[1]),1)


# main --------------------------------------------------------------------------------------------
def main(args):

    running = True
    sim = False

    draggingStart = False
    draggingEnd = False
    preClicked = False

    while running:


        # exit game loop if cross is clicked or escape key is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # everything in this sets the algorithm and lets you move the start/end positions and make walls
        if not sim:
            # get mouse inputs
            pressed = pygame.mouse.get_pressed()[0] # get left mouse button state
            mpos = pygame.mouse.get_pos() # get mouse position

            if pressed:
                # if clicking, and mouse is on start or end squares, check if it moves off while still clicking. if it does, move the start or end square to the new cursor position
                if (mpos[0]//cellWH) == start[0] and (mpos[1]//cellWH) == start[1]:
                    draggingStart = True
                elif draggingStart:
                    start[0] = mpos[0]//cellWH
                    start[1] = mpos[1]//cellWH

                elif (mpos[0]//cellWH) == end[0] and (mpos[1]//cellWH) == end[1]:
                    draggingEnd = True
                elif draggingEnd:
                    end[0] = mpos[0]//cellWH
                    end[1] = mpos[1]//cellWH

                elif not preClicked:
                    grid[mpos[1]//cellWH][mpos[0]//cellWH] = not grid[mpos[1]//cellWH][mpos[0]//cellWH]
                    preClicked = True

            else:
                # reset all clicking variables when the mouse isnt clicking
                draggingEnd = False
                draggingStart = False
                preClicked = False

        else:
            # the actual algorithm!! --------------------------------------------------------------
            open_nodes = [start.copy()]
            closed_nodes = []

            for node in open_nodes:
                pass

        # clear window
        root.fill(bgColour)

        # draw the grid (if you couldn't work out that, close the tab. now!)
        drawGrid()

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