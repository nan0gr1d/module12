#  module_12_1
#  https://github.com/yanchuki/HumanMoveTest/blob/master/runner.py

import unittest

#, is_frozen = False

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
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('runner1')
        for _ in range(10):
            runner.walk()
        super().assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('runner2')
        for _ in range(10):
            runner.run()
        super().assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = Runner('runner3')
        runner2 = Runner('runner4')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        super().assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
