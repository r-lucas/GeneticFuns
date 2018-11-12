from RunThing import *
import pygame
import sys


def main():
    print("Starting!")

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    run = RunThing(screen)
    white = (255, 255, 255)
    clock = pygame.time.Clock()
    while True:
        screen.fill(white)
        #print("Drawing!")
        run.draw()
        #print("done drawing")
        msElapsed=clock.tick(60)
        pygame.display.update()
        #print("updated")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

main()
