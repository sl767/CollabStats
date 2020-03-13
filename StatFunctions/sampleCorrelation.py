from StatFunctions.covariance import Covariance
from StatFunctions.standardDeviation import StandardDeviation
from RandomGenerator.numbersFromSeedList import PickNumbersSeed


class SampleCorrelation():
    @staticmethod
    def correlation(theSeed, dataA, dataB):
        # getting sample from population
        sampleDataA = PickNumbersSeed.pickNumbers(theSeed, dataA, 5)
        sampleDataB = PickNumbersSeed.pickNumbers(theSeed, dataB, 5)

        cov = Covariance.covariance(sampleDataA, sampleDataB)
        stdDevA = StandardDeviation.standardDeviation(sampleDataA)
        stdDevB = StandardDeviation.standardDeviation(sampleDataB)
        return cov/(stdDevA*stdDevB)