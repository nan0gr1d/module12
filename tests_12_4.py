#  module_12_4
#  https://github.com/yanchuki/HumanMoveTest/blob/master/rt_with_exceptions.py

import rt_with_exceptions as rt
import unittest
import logging

logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = rt.Runner('runner1', speed=-1)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner = rt.Runner(['runner2'])
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner1 = rt.Runner('runner3')
        runner2 = rt.Runner('runner4')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
