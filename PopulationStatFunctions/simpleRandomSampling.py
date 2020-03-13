from RandomGenerator.numbersFromSeedList import PickNumbersSeed

from numpy.random import seed


class SimpleRandomSampling(PickNumbersSeed):
    @staticmethod
    def generateSampling(theSeed, aList, rangeNum):
        seed(theSeed)
        return PickNumbersSeed.pickNumbers(theSeed, aList, rangeNum)