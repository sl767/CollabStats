import random


class Random:
    @staticmethod
    def randomInt(number1, number2):
        if isinstance(number1, float):
            return Random.randomFloat(number1, number2)
        return random.randint(number1, number2)

    @staticmethod
    def randomFloat(number1, number2):
        return random.uniform(number1, number2)
