import unittest
from tests.register_test import RegisterTest
from tests.login_test import LoginTest
from tests.basket_test import BasketTest

loader = unittest.TestLoader()
test_classes = [RegisterTest, LoginTest, BasketTest]
test_suites = []

for test_class in test_classes:
    tests = loader.loadTestsFromTestCase(test_class)
    test_suites.append(tests)

test_suite = unittest.TestSuite(test_suites)

unittest.TextTestRunner(verbosity=2).run(test_suite)
