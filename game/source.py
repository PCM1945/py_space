#sizey  -20 to 700
#sizex 0- 680
# ************space game*****************
# import libs
import math
import pygame
from pygame.locals import *

# initialize screen
pygame.init()
width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
# setting key array
keys = [False, False, False, False, False]
# setting initial x,y player position
playerpos = [100.00, 100.00]
correction = 0


def main():
    # list to keep the coordinates of missiles
    projectiles = []

    # loading player resource
    player = pygame.image.load("resources\ship_hero.png")
    shot = pygame.image.load("resources\ire.png")
    background = pygame.image.load("resources\scene.jpg")
    # loop forever
    while 1:
        # clear the screen before drawing again
        screen.fill(0)
        # draw the screen elements
        screen.blit(player, (playerpos, playerpos))
        # update the screen
        pygame.display.flip()
        # loop through the events
        for event in pygame.event.get():
            # check if the event is a key button
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    keys[0] = True
                if event.key == K_LEFT:
                    keys[1] = True
                if event.key == K_DOWN:
                    keys[2] = True
                if event.key == K_RIGHT:
                    keys[3] = True
                if event.key == K_SPACE:
                    keys[4] = True
            if keys[0]:
                playerpos[1] -= 20
            if keys[2]:
                playerpos[1] += 20
            if keys[1]:
                playerpos[0] -= 20
            if keys[3]:
                playerpos[0] += 20
            if keys[4]:
               #*********logic to fire ******
                # changing playerpos to firepos
                fire_position = playerpos
                # protecting fire_position values
                valx = fire_position[0]
                valy = fire_position[1]
               # print("valx:" + str(valx))
            # ADD THE NEW POSITION TO VALX
                while valx < 680:
                    valx = valx + 20
                   # screen.blit(background, valx, valy)
                    screen.blit(shot, (valx+100, valy+90))
                    pygame.display.flip()
                    screen.fill(1)
                    if valx > 700:
                        valx = 0
            if event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    keys[4] = False
                if event.key == pygame.K_UP:
                    keys[0] = False
                if event.key == pygame.K_LEFT:
                    keys[1] = False
                if event.key == pygame.K_DOWN:
                    keys[2] = False
                if event.key == pygame.K_RIGHT:
                    keys[3] = False
                    # Moving player
                projectiles.clear()
                if event.type == pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)


if __name__ == '__main__':
    main()