import sys
import unittest
from io import StringIO
from third_challenge import Printer


class TestPrintedOutPut(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()  # Listener
        self.printer = Printer()

    def test_value_name(self):
        self.printer.set_value('John Doe')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'John Doe')

    def test_value_job(self):
        self.printer.set_value('Boxer')
        self.printer.print_value()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Boxer')
        # Todo: use assertEqual to check if the printed string is 'Boxer'

    def tearDown(self):
        self.printer = None


if __name__ == '__main__':
    unittest.main()
