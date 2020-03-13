from StatFunctions.zScore import Z_score
from PopulationStatFunctions.marginOfError import MarginOfError
from mathOperations.exponent import Exponent

class SampleSizeUnkPopul():
    @staticmethod
    def sampleSize(theSeed, data, percentage):
        z = Z_score.z_score(theSeed, data)
        e = MarginOfError.margin(theSeed, data)
        p = percentage
        q = 1 - p
        val = z/e
        sample = Exponent.power(val, 2) * p * q

        return sample