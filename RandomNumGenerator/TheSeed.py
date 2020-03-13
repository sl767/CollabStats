import random
from RandomGenerator.pickRandom import PickRandomly

class TheSeed():
    @staticmethod
    def pickSeed(Seed, aList):
        random.seed(Seed)

        return PickRandomly.pick(aList)