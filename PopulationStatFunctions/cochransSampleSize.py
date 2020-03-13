from StatFunctions.zScore import Z_score
from PopulationStatFunctions.marginOfError import MarginOfError
from StatFunctions.population_Proportion import PopulationProportion
from mathOperations.exponent import Exponent


class Cochran():
    @staticmethod
    def cochran(theSeed, data, rangeNumber):
        # z = z-score
        # p = proportion population
        # e = margin of error

        z = Z_score.z_score(theSeed, data)
        p = PopulationProportion.proportion(theSeed, data, rangeNumber)
        e = MarginOfError.margin(theSeed, data)
        q = 1 - p

        cochran = (Exponent.power(z,2) * p * q)/Exponent.power(e,2)

        return cochran