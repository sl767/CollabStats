from scipy.stats import sem, t
from StatFunctions.mean import Mean

class ConfIntervalPopulation():
    @staticmethod
    def confidenceInterval(confidence, data):

        lenData = len(data)
        mean = Mean.mean(data)
        std_err = sem(data)
        high = std_err * t.ppf((1 + confidence) / 2, lenData - 1)

        start = mean - high
        end = mean + high

        return start, end