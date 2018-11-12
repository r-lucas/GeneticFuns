from Brain import *
import math
import pygame


class Dot:

    def __init__(self, dotSize, boxSize, screen, goal):
        self.brain = Brain(1000)  # new brain with 1000 instructions
        # print self.brain.directions
        self.brain.randomize()
        # start the dots at the bottom of the window with a no velocity or acceleration
        self.pos = [boxSize[0]/2, boxSize[1] - 10]
        self.vel = [0, 0]
        self.acc = [0, 0]
        self.dotSize = dotSize
        self.boxSize = boxSize
        self.screen = screen
        self.goal = goal

        self.dead = False
        self.reachedGoal = False
        self.isBest = False

        self.fitness = 0

        self.green = (0, 255, 0)
        self.black = (0, 0, 0)

        self.color = self.black

        self.maxSpeed = 5


    # ---------------------------------------------------------------------------------------------------------------
    # draws the dot on the screen
    def show(self):
        # if this dot is the best dot from the previous generation then draw it as a big green dot

        if self.isBest:
            self.color = self.green
            self.dotSize = 8
        else:
            # all other dots are just smaller black dots
            self.color = self.black
            self.dotSize = 4

        pygame.draw.circle(self.screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.dotSize, 0)

    # -----------------------------------------------------------------------------------------------------------------
    # moves the dot according to the brains directions

    def move(self):

        if len(self.brain.directions) > self.brain.step:
            # if there are still directions left then set the acceleration as the next PVector in the direcitons array
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step = self.brain.step + 1
        else:  # if at the end of the directions array then the dot is dead
            self.dead = True

        # apply the acceleration and move the dot
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        if math.fabs(self.vel[0]) > self.maxSpeed:
            self.vel[0] = math.copysign(self.maxSpeed, self.vel[0])  # not too fast
        if math.fabs(self.vel[1]) > self.maxSpeed:
            self.vel[1] = math.copysign(self.maxSpeed, self.vel[1])

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    # ---------------------------------------------------------------------------------------------------------------
    # calls the move function and check for collisions and stuff
    def update(self):
        if not self.dead and not self.reachedGoal:
            self.move()
        if self.pos[0] < 2 or self.pos[1] < 2 or self.pos[0] > self.boxSize[0]-2 or self.pos[1] > self.boxSize[1] - 2:
            # if near the edges of the window then kill it
            self.dead = True
        elif math.sqrt((self.goal[0]-self.pos[0])**2 + (self.goal[1]-self.pos[1])**2) < 5:  # if reached goal
            self.reachedGoal = True
        elif self.pos[0] >= 0 - 2 and self.pos[0] <= 600+2 and self.pos[1] >= 600-2 and self.pos[1] <= 610+2:
            self.dead = True
        elif self.pos[0] >= 200 - 2 and self.pos[0] <= 800 + 2 and self.pos[1] >= 300 - 2 and self.pos[1] <= 310 + 2:
            self.dead = True

    # -------------------------------------------------------------------------------------------------------------------
    # calculates the fitness
    def calculateFitness(self):
        if self.reachedGoal:
            # if the dot reached the goal then the fitness is based on the amount of steps it took to get there
            self.fitness = 1.0/16.0 + 10000.0/(self.brain.step * self.brain.step)
        else: # if the dot didn't reach the goal then the fitness is based on how close it is to the goal
            distanceToGoal = math.sqrt((self.goal[0]-self.pos[0])**2 + (self.goal[1]-self.pos[1])**2)
            # distanceToGoal = dist(self.pos(0), self.pos(1), goal.x, goal.y);
            fitNum = 1.0/(distanceToGoal * distanceToGoal)**2
            self.fitness = fitNum

    # -----------------------------------------------------------------------------------------------------------------
    # clone it
    def gimmeBaby(self):
        baby = Dot(self.dotSize, self.boxSize, self.screen, self.goal)
        baby.brain = self.brain.clone()
        # babies have the same brain as their parents
        return baby

