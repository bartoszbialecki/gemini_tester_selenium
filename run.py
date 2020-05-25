import unittest
from tests.register_test import RegisterTest
from tests.login_test import LoginTest

register_tests = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)

test_suite = unittest.TestSuite(register_tests)

unittest.TextTestRunner(verbosity=2).run(test_suite)
