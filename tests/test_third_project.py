import unittest
import sys
from io import StringIO
from third_project import Profile


class TestPrintedOutput(unittest.TestCase):

    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO() # Listener
        self.profile = Profile('Andrey', 33, 'student')

    def test_name(self):
        self.profile.print_name()
        self.assertEqual(sys.stdout.getvalue().strip(), 'Andrey')

    def test_age(self):
        self.profile.print_age()
        self.assertEqual(sys.stdout.getvalue().strip(), str(33))

    def test_job(self):
        self.profile.print_job()
        self.assertEqual(sys.stdout.getvalue().strip(), 'student')

    def tearDown(self):
        self.profile = None
