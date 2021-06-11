import unittest
from tests.test_fifth_project_tdd import TestCalculate
from tests.test_fifth_project_tdd import TestGetNetWorth

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculate('test_calculate_easy_first'))
    suite.addTest(TestCalculate('test_calculate_medium_second'))
    suite.addTest(TestCalculate('test_calculate_hard_first'))

    suite.addTest(TestGetNetWorth('test_net_worth_easy_first'))
    suite.addTest(TestGetNetWorth('test_net_worth_easy_second'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())