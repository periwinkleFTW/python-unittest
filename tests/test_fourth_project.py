import unittest
import time
from fourth_project import FibonacciSequence


class TestEfficiency(unittest.TestCase):

    def setUp(self):
        self._fibonacci_sequence = FibonacciSequence()
        self._efficiency_data = dict()

    def test_first_method(self):
        starting_time = time.time()
        self._fibonacci_sequence.recursive_method(10)
        ending_time = time.time()

        self._efficiency_data['recursive_method'] = ending_time - starting_time

        print (self._efficiency_data)

    def test_second_method(self):
        starting_time = time.time()
        self._fibonacci_sequence.math_method(10)
        ending_time = time.time()

        self._efficiency_data['math_method'] = ending_time - starting_time

        print(self._efficiency_data)

    def tearDown(self):
        pass