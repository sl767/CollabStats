from StatFunctions.standardDeviation import StandardDeviation
from StatFunctions.zScore import Z_score


class MarginOfError():
    @staticmethod
    def margin(theSeed, data):
        z_score = Z_score.z_score(theSeed, data)
        stdDev = StandardDeviation.standardDeviation(data)
        return z_score * stdDev