import time
import unittest
from fourth_challenge import EfficiencyAdding


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._efficiency = EfficiencyAdding()
        self._efficiency_data = dict()

    def test_first_adding_method(self):
        starting_time = time.time()
        self._efficiency.adding_two_first_method(1000000)
        ending_time = time.time()

        self._efficiency_data['first_method'] = ending_time - starting_time

    def test_second_adding_method(self):
        starting_time = time.time()
        self._efficiency.adding_two_second_method(1000000)
        ending_time = time.time()

        self._efficiency_data['second_method'] = ending_time - starting_time

    def tearDown(self):
        print(self._efficiency_data)
        self._efficiency = None


if __name__ == '__main__':
    unittest.main()