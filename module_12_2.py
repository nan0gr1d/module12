#  module_12_2
#  https://github.com/yanchuki/HumanMoveTest/blob/master/runner_and_tournament.py

import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runn1 = Runner('Усэйн',10)
        self.runn2 = Runner('Андрей', 9)
        self.runn3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            for place, runner in result.items():
                print(f"{place}: {str(runner)}  ", end='')
            print()

    def test_tourn1(self):
        tour = Tournament(90, self.runn1, self.runn3)
        TournamentTest.all_results.append(tour.start())
        self.assertTrue(str(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])]) == 'Ник')

    def test_tourn2(self):
        tour = Tournament(90, self.runn2, self.runn3)
        TournamentTest.all_results.append(tour.start())
        self.assertTrue(str(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])]) == 'Ник')

    def test_tourn3(self):
        tour = Tournament(90, self.runn1, self.runn2, self.runn3)
        TournamentTest.all_results.append(tour.start())
        self.assertTrue(str(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])]) == 'Ник')


if __name__ == "__main__":
    unittest.main()
