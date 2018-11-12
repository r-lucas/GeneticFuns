from Dot import *
import random


class Population:

    def __init__(self, size, dotSize, boxSize, screen, goal):
        self.dotSize = dotSize
        self.boxSize = boxSize
        self.screen = screen
        self.goal = goal
        self.dots = [Dot(dotSize, boxSize, screen, goal) for i in xrange(size)]
        self.fitnessSum = 0
        self.gen = 1
        self.bestDot = 0  # the index of the best dot in the dots set
        self.minStep = 10000
        self.newDots = 0

    # ---------------------------------------------------------------------------------------------------------------
    # show all dots
    def show(self):
        for doti in self.dots:
            doti.show()
        # self.dots[0].show()

    # ------------------------------------------------------------------------------------------------------------------
    # update all dots
    def update(self):
       # if self.dots[0].brain.step % self.minStep-1 == 0:
       #     print ("At step", self.dots[0].brain.step)
        i = 0
        for doti in self.dots:
            if doti.brain.step > self.minStep:
                # if the dot has already taken more steps than the best dot has taken to reach the goal
                self.dots[i].dead = True # then it dead
            else:
                self.dots[i].update()
            i = i+1

    # ----------------------------------------------------------------------------------------------------------------
    #calculate all the fitnesses
    def calculateFitness(self):
        for doti in self.dots:
            doti.calculateFitness()

    # ----------------------------------------------------------------------------------------------------------------
    # returns whether all the dots are either dead or have reached the goal
    def allDotsDead(self):
        for doti in self.dots:
            if not doti.dead and not doti.reachedGoal:
                return False

        return True

    # -------------------------------------------------------------------------------------------------------------
    # you get it
    def calculateFitnessSum(self):
        self.fitnessSum = 0
        for doti in self.dots:
            self.fitnessSum += doti.fitness

    # ----------------------------------------------------------------------------------------------------------------
    # chooses dot from the population to return randomly(considering fitness)
    # this function works by randomly choosing a value between 0 and the sum of all the fitnesses
    # then go through all the dots and add their fitness to a running sum and
    # if that sum is greater than the random value generated that dot is chosen
    # since dots with a higher fitness function add more to the running sum they have a higher chance of being chosen
    def selectParent(self):
        rand = random.random()*self.fitnessSum
        runningSum = 0
        for doti in self.dots:
            runningSum += doti.fitness
            if runningSum > rand:
                return doti
        # should never get to this point
        return 0

    # ----------------------------------------------------------------------------------------------------------------
    # mutates all the brains of the babies
    def mutateDemBabies(self):
        i = 0
        for doti in self.dots:
            self.dots[i].brain.mutate()
            i = i+1
        return 0

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # finds the dot with the highest fitness and sets it as the best dot
    def setBestDot(self):
        max = 0
        maxIndex = 0
        i = 0
        for doti in self.dots:
            # print doti.fitness
            if doti.fitness > max:
                max = doti.fitness
                maxIndex = i
            i = i+1

        self.bestDot = maxIndex
        self.dots[maxIndex].isBest = True
        print("bestDot: ", self.bestDot)

        # if this dot reached the goal then reset the minimum number of steps it takes to get to the goal
        if self.dots[self.bestDot].reachedGoal:
            self.minStep = self.dots[self.bestDot].brain.step
            print("step:", self.minStep)

        # ----------------------------------------------------------------------------------------------------------------
        # gets the next generation of dots
    def naturalSelection(self):
        self.newDots = 0
        self.newDots = [Dot(self.dotSize, self.boxSize, self.screen, self.goal) for i in xrange(len(self.dots))]
        # newDots = Dot[dots.length] #next gen
        self.setBestDot()
        self.calculateFitnessSum()

        # the champion lives on

        i = 0
        for doti in self.newDots:
            # select parent based on fitness
            parent = self.selectParent()

            # get baby from them
            self.newDots[i] = parent.gimmeBaby()
            i = i + 1

        self.newDots[0] = self.dots[self.bestDot].gimmeBaby()
        self.newDots[0].isBest = True
        self.dots = self.newDots
        self.gen = self.gen + 1
