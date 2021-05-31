import unittest
from first_challenge import counter


class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        # Todo: make sure that your program returns 2 given the string 'Mo'
        self.assertEqual(counter('Mo'), 2)
        pass

    def test_easy_input_two(self):
        # Todo: make sure that your program returns 8 given the string 'Mohammad'
        self.assertEqual(counter('Mohammad'), 8)
        pass


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        # Todo: make sure that the program raises an exception whenever there is any non-english charts. Ex. !@#$%^.
        with self.assertRaises(Exception):
            self.assertEqual(counter('Mo%$#%#'), 2)


    def test_medium_input_two(self):
        # Todo: make sure that your program does not count paces. It should only count english alpha.
        self.assertEqual(counter('Andrey Andrey'), 12)


class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        # Todo: make sure that the program raises an exception whenever an empty string is given.
        with self.assertRaises(Exception):
            self.assertEqual(counter(' '), 0)
            self.assertEqual(counter(''), 0)

    def test_hard_input_two(self):
        # Todo: make sure that your program does not accept a None input.
        with self.assertRaises(Exception):
            self.assertEqual(counter(None), 0)


if __name__ == '__main__':
    unittest.main()
