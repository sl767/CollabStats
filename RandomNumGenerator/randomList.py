from numpy.random import seed
import random


def listOfFloats(number1, number2, length, Seed):
    pass


class RandomList():

    @staticmethod
    def listOfFloats(number1, number2, length, Seed):
        aList = []
        seed(Seed)

        for each in range(length):
            number = random.uniform(number1, number2)
            aList.append(number)

        return aList


    @staticmethod
    def listOfInts(number1, number2, length, Seed):
        if isinstance(number1, float):
            return listOfFloats(number1, number2, length, Seed)

        aList = []
        seed(Seed)

        for each in range(length):
            number = random.randint(number1, number2)
            aList.append(number)

        return aList
