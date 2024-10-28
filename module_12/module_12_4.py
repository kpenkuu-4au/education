import logging
import unittest

logging.basicConfig(
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(levelname)s | %(message)s | line %(lineno)s',
    level=logging.INFO)


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str) or name is None:
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self, test_runner=None):
        try:
            runner_1 = Runner('test', -13)
            test_runner = Runner(test_runner)
            for run in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info(msg='"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner')

    def test_run(self, test_runner=None):
        try:
            runner_1 = Runner([7, 7, 7])
            test_runner = Runner(test_runner)
            for run in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info(msg='"test_run" выполнен успешно')
        except TypeError:
            logging.warning(msg='Неверный тип данных для объекта Runner')

    def test_challenge(self, runner1=None, runner2=None):
        runner1 = Runner(runner1)
        runner2 = Runner(runner2)
        for run in range(10):
            runner1.run()
        for run in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
