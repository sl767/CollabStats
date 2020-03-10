import random
from RandomNumGenerator.numbersFromList import PickNoSeed

class PickNumbersSeed():
    @staticmethod
    def pickNumbers(theSeed, aList, rangeNum):
        random.seed(theSeed)

        newList = PickNoSeed.pickNumbers(aList, rangeNum)
        return newList