import random


class RandomSeed:
    @staticmethod
    def randomInt(Seed, number1, number2):
        random.seed(Seed)
        if isinstance(number1, float):
            return RandomSeed.randomFloat(Seed, number1, number2)
        return random.randint(number1, number2)

    @staticmethod
    def randomFloat(Seed, number1, number2):
        random.seed(Seed)
        randNumb = random.uniform(number1, number2)

        return randNumb
