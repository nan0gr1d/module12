#  suite_12_3

import unittest
import tests_12_3     #   https://github.com/nan0gr1d/module12/blob/master/tests_12_3.py


test_ST = unittest.TestSuite()
test_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

suite_runner = unittest.TextTestRunner(verbosity=2)
suite_runner.run(test=test_ST)
