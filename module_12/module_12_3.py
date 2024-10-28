import unittest

import suite_12_3

test_t = unittest.TestSuite()
test_t.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.TournamentTest))
test_t.addTest(unittest.TestLoader().loadTestsFromTestCase(suite_12_3.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_t)
