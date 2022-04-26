import unittest
from tc.test_cases_1 import test_cases_1
from tc.test_cases_2 import test_cases_2
from tc.test_cases_3 import test_cases_3
from tc.test_cases_4 import test_cases_4
from tc.test_cases_5 import test_cases_5


tc1 = unittest.TestLoader().loadTestsFromTestCase(test_cases_1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_cases_2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(test_cases_3)
tc4 = unittest.TestLoader().loadTestsFromTestCase(test_cases_4)
tc5 = unittest.TestLoader().loadTestsFromTestCase(test_cases_5)

masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
