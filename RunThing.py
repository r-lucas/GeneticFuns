from Population import *
import pygame
import time


class RunThing:

    def __init__(self, screen):
        self.goal = [400, 10]
        self.boxSize = [800, 800]
        self.dotSize = 4
        self.screen = screen
        self.test = Population(100, self.dotSize, self.boxSize, self.screen, self.goal)

    def draw(self):
        # draw goal
        # print("drawing the thing")
        pygame.draw.circle(self.screen, (255, 0, 0),  (self.goal[0], self.goal[1]), 10, 0)

        pygame.draw.rect(self.screen, (0, 0, 255), (0, 600, 600, 10), 0)
        pygame.draw.rect(self.screen, (0, 255, 255), (200, 300, 600, 10), 0)

        if self.test.allDotsDead():
            # genetic algorithm
            self.test.calculateFitness()
            self.test.naturalSelection()
            self.test.mutateDemBabies()

        else:
            # if any of the dots are still alive then update and then show them
            self.test.update()
            self.test.show()
            # time.sleep(1)
            #print "showing frame"
            #print("showed the thing")

