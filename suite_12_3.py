import logging
import unittest
import runner_and_tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf((is_frozen), 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            walk1 = runner_and_tournament.Runner('Иван')
            for i in range(10):
                walk1.walk()
            self.assertEqual(walk1.distance, 50)
        except logging.warning:
            print("Неверная скорость для Runner")

    @unittest.skipIf((is_frozen), 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            logging.info('"test_walk" выполнен успешно')
            walk2 = runner_and_tournament.Runner('Максим')
            for i in range(10):
                walk2.run()
            self.assertEqual(walk2.distance, 100)
        except logging.warning:
            print("Неверный тип данных для объекта Runner")


    @unittest.skipIf((is_frozen), 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walk3 = runner_and_tournament.Runner('Ваня')
        walk4 = runner_and_tournament.Runner('Ваня1')
        for distance in range(10):
            walk3.run()
            walk4.walk()
        self.assertNotEqual(walk3.distance, walk4.distance)
class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.y = runner_and_tournament.Runner('Усэйн', 10)
        self.a = runner_and_tournament.Runner('Андрей', 9)
        self.n = runner_and_tournament.Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for x, all_value in cls.all_results.items():
            slovar = {}
            for key, value in all_value.items():
                znach = {key: value.name}
                slovar.update(znach)
            print(slovar)


    @unittest.skipIf((is_frozen),'Тесты в этом кейсе заморожены')
    def test_1(self):
        g = runner_and_tournament.Tournament(90, self.y, self.n)
        self.distance = g.start()
        self.all_results['Первый забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    @unittest.skipIf((is_frozen), 'Тесты в этом кейсе заморожены')
    def test_2(self):
        s = runner_and_tournament.Tournament(90, self.a, self.n)
        self.distance = s.start()
        self.all_results['Второй забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

    @unittest.skipIf((is_frozen), 'Тесты в этом кейсе заморожены')
    def test_3(self):
        z = runner_and_tournament.Tournament(90, self.y, self.a, self.n)
        self.distance = z.start()
        self.all_results['Третий забег'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Ник')

if __name__ == '__main__':
    unittest.main()