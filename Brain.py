import random
import math


class Brain:

    def __init__(self, size):
        self.directions = [[0, 0] for i in xrange(size)]
        #print self.directions
        self.step = 0

    # -----------------------------------------------------------------------------------------------------------
    # sets all the vectors in directions to a random vector with length 1
    def randomize(self):
        i = 0
        for direction in self.directions:
            randomAngle = random.random() * 2 * math.pi
            direction= (math.cos(randomAngle), math.sin(randomAngle))
            self.directions[i] = direction
            i = i + 1

    # ---------------------------------------------------------------------------------------------------------
    # returns a perfect copy of this brain object
    def clone(self):
        clone = Brain(len(self.directions))
        i = 0
        for direction in self.directions:
            clone.directions[i] = direction
            i = i + 1

        return clone

    # -----------------------------------------------------------------------------------------------------------
    # mutates the brain by setting some of the directions to random vectors
    def mutate(self):
        mutationRate = 0.01 # chance that any vector in directions gets changed
        i = 0
        for direction in self.directions:
            rand = random.random()
            if rand < mutationRate:
                # set this direction as a random direction
                randomAngle = random.random() * 2 * math.pi
                self.directions[i] = (math.cos(randomAngle), math.sin(randomAngle))
            i = i + 1



