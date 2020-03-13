from scipy.stats import sem, t

from PopulationStatFunctions.confidenceIntervalForPopulation import ConfIntervalPopulation
from PopulationStatFunctions.simpleRandomSampling import SimpleRandomSampling


class ConfIntervalSample(ConfIntervalPopulation):
    @staticmethod
    def confidenceInterval(confidence, data, theSeed, higher):
        newSample = SimpleRandomSampling.generateSampling(theSeed, data, higher)
        return ConfIntervalPopulation.confidenceInterval(confidence, newSample)