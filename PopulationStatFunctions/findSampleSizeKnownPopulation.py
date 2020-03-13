from StatFunctions.zScore import Z_score
from PopulationStatFunctions.marginOfError import MarginOfError
from StatFunctions.standardDeviation import StandardDeviation
from mathOperations.exponent import Exponent

class SampleSizeKnown():
    @staticmethod
    def sampleSize(theSeed, data):
        z = Z_score.z_score(theSeed, data)
        e = MarginOfError.margin(theSeed, data)
        stdDev = StandardDeviation.standardDeviation(data)
        val = (z * stdDev) / e
        sample = Exponent.power(val, 2)

        return sample