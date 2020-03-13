import unittest
from random import seed
from numpy.random import randint

from RandomNumGenerator.RNG_withoutseed import Random
from RandomNumGenerator.RNG_withseed import RandomSeed
from RandomNumGenerator.randomList import RandomList
from RandomNumGenerator.pickRandom import PickRandomly
from RandomNumGenerator.TheSeed import TheSeed
from RandomNumGenerator.numbersFromList import PickNoSeed
from RandomNumGenerator.numberFromSeedList import PickNumbersSeed




class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mySeed = seed(3)
        self.aList = randint(0, 20, 10)


    def test_Random_No_Seed_Int(self):
        result = Random.randomInt(0, 10)
        self.assertEqual(isinstance(result, int), True)

    def test_Random_No_Seed_Float(self):
        result = Random.randomFloat(0, 10)
        self.assertEqual(isinstance(result, float), True)

    def test_Random_Seed_Int(self):
        result = RandomSeed.randomInt(3, 0, 10)
        result2 = RandomSeed.randomInt(3, 0, 10)
        self.assertEqual(result, result2)

    def test_Random_Seed_Float(self):
        result = RandomSeed.randomFloat(3, 0, 10)
        result2 = RandomSeed.randomFloat(3, 0, 10)
        self.assertEqual(result, result2)


    def test_Make_List_Ints(self):
        result = RandomList.listOfInts(0, 10, 10, 3)
        self.assertEqual(result, [3, 9, 8, 2, 5, 9, 7, 10, 9, 1])

    def test_Make_List_Floats(self):
        result = RandomList.listOfFloats(0, 10, 10, 3)
        self.assertEqual(result, [2.3796462709189137, 5.442292252959518, 3.6995516654807927, 6.039200385961944, 6.25720304108054,
                                  0.6552885923981311, 0.13167991554874137, 8.3746908209646, 2.5935401432800766, 2.3433096104669637])

    def test_Pick_Random_Number(self):
        myList = RandomList.listOfInts(0, 10, 10, 3)
        result = PickRandomly.pick(myList)
        self.assertEqual(result, 1)

    def test_Pick_Number_With_Seed(self):
        myList = RandomList.listOfInts(0, 10, 10, 3)
        result = TheSeed.pickSeed(3, myList)
        self.assertEqual(result, 2)

    def test_N_numbers_from_List(self):
        myList = RandomList.listOfInts(0, 10, 10, 3)
        result = PickNoSeed.pickNumbers(myList, 5)
        self.assertEqual(result, [1, 3, 10, 5, 9])

    def test_N_numbers_from_list_seed(self):
        myList = RandomList.listOfInts(0, 10, 10, 3)
        result = PickNumbersSeed.pickNumbers(3, myList, 5)
        self.assertEqual(result, [2, 1, 9, 8, 9])





if __name__ == '__main__':
    unittest.main()