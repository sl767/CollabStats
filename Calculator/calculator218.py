from mathOperations.addition import Addition
from mathOperations.subtraction import Subtraction
from mathOperations.multiplication import Multiplication
from mathOperations.division import Division
from mathOperations.exponent import Exponent
from mathOperations.logarithm import Logarithm
from mathOperations.sqrRoot import SquareRoot

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def SumList(self,a):
        self.Result = Addition.sumList(a)
        return self.Result

    def Difference(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result

    def Multiplication(self,a,b):
        self.Result = Multiplication.product(a,b)
        return self.Result

    def Division(self,a,b):
        self.Result = Division.quotient(a,b)
        return self.Result

    def Exponent(self,a,b):
        self.Result = Exponent.power(a,b)
        return self.Result

    def Logarithm(self,a,b):
        self.Result = Logarithm.logarithm(a,b)
        return self.Result

    def SquareRoot(self,a):
        self.Result = SquareRoot.root(a)
        return self.Result