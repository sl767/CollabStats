from RandomNumGenerator.numberFromSeedList import PickNumbersSeed

class PopulationProportion():
    @staticmethod
    def proportion(theSeed, data, rangeNumber):
        subData = PickNumbersSeed.pickNumbers(theSeed, data, rangeNumber)
        proportion = len(subData)/len(data)
        return proportion