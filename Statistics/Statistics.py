from Calculator.Calculator import Calculator
from StatFunctions.mean import Mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = Mean
        return self.result