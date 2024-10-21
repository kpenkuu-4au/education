import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self, test_runner=None):
        test_runner = Runner(test_runner)
        for run in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)

    def test_run(self, test_runner=None):
        test_runner = Runner(test_runner)
        for run in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self, runner1=None, runner2=None):
        runner1 = Runner(runner1)
        runner2 = Runner(runner2)
        for run in range(10):
            runner1.run()
        for run in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
