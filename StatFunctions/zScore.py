from RandomGenerator.TheSeed import TheSeed
from StatFunctions.standardDeviation import StandardDeviation
from StatFunctions.mean import Mean

class Z_score():
    @staticmethod
    def z_score(theSeed, data):
        X = TheSeed.pickSeed(theSeed, data)
        mean = Mean.mean(data)
        stdDev = StandardDeviation.standardDeviation(data)
        return (X-mean)/stdDev