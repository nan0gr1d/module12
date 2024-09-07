#  suite_12_3

import unittest
import module_12_1   #  https://github.com/nan0gr1d/module12/blob/master/module_12_1.py
import module_12_2   #  https://github.com/nan0gr1d/module12/blob/master/module_12_2.py


test_ST = unittest.TestSuite()
test_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
test_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

suite_runner = unittest.TextTestRunner(verbosity=2)
suite_runner.run(test=test_ST)
