import timeit
from unittest import TestCase
import DiGraph, GraphAlgo, GraphInterface, GraphAlgoInterface, Node, Edge
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node import Node


class comperation(TestCase):

    def test_load_from_json(self):
        start = timeit.default_timer()

        file1 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A1.json"
        g_algo1 = GraphAlgo()
        self.assertTrue(g_algo1.load_from_json(file1))

        file4 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A4.json"
        g_algo4 = GraphAlgo()
        self.assertTrue(g_algo4.load_from_json(file4))

        fileT = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A5.json"
        g_algoT = GraphAlgo()
        self.assertTrue(g_algoT.load_from_json(fileT))
        stop = timeit.default_timer()

        print('Load Time: ', stop - start)

    def test_save_to_json(self):
        start = timeit.default_timer()
        file1 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        self.assertTrue(g_algo1.save_to_json('A1_new'))

        file4 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        self.assertTrue(g_algo4.save_to_json('A4_new'))

        fileT = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A5.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        self.assertTrue(g_algoT.save_to_json('T0_new'))
        stop = timeit.default_timer()

        print('Save Time: ', stop - start)

    def test_shortest_path(self):
        start = timeit.default_timer()
        file1 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        self.assertEqual(g_algo1.shortest_path(0, 8), (0.9046810940028001, [0, 8]))
        self.assertEqual(g_algo1.shortest_path(5, 16), (2.3862978099481547, [5, 25, 16]))

        file4 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        self.assertEqual(g_algo4.shortest_path(8, 25), (3.3560955442187255, [8, 0, 16, 25]))
        self.assertEqual(g_algo4.shortest_path(1, 39), (1.4687246563734302, [1, 10, 39]))

        fileT = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A5.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        self.assertEqual(g_algoT.shortest_path(0, 3), (2.4826674989991067, [0, 2, 3]))
        self.assertEqual(g_algoT.shortest_path(1, 2), (1.3230130106118398, [1, 9, 2]))
        stop = timeit.default_timer()

        print('Shortest path Time: ', stop - start)

    def test_centerPoint(self):
        start = timeit.default_timer()
        file1 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        ans1, min1 = 41, 8.506995383843982
        self.assertEqual(g_algo1.centerPoint(), (ans1, min1))

        file4 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        ans4, min4 = 41, 8.506995383843982
        self.assertEqual(g_algo4.centerPoint(), (ans4, min4))

        fileT = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A5.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        ansT, minT = 41, 8.506995383843982
        self.assertEqual(g_algoT.centerPoint(), (ansT, minT))
        stop = timeit.default_timer()

        print('Center Time: ', stop - start)

    def test_TSP(self):
        start = timeit.default_timer()

        file1 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        self.assertEqual(g_algo1.TSP([10, 2, 16]), ([10, 9, 8, 7, 6, 2, 3, 1, 0, 16], 108.1126437071901))
        self.assertEqual(g_algo1.TSP([5,3,12,14]),( [5, 4, 3, 2, 1, 0, 16, 15, 14, 15, 13, 12], 162.16896556078518))

        file4 = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        self.assertEqual(g_algo4.TSP([1,20,28,34]), ([1, 2, 30, 28, 31, 32, 33, 34, 35, 7, 6, 15, 16, 19, 20], 459.32074371556615))
        self.assertEqual(g_algo4.TSP([5,11,21,22,24,30,35]),([5, 25, 24, 23, 22, 21, 0, 1, 2, 30, 31, 32, 33, 35, 36, 8, 9, 10, 11],
        918.6414874311324))

        fileT = r"C:\Users\tairm\PycharmProjects\Ex3\src\data\A5.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        self.assertEqual(g_algoT.TSP([0,3,39]), ([0, 2, 3, 4, 12, 10, 39], 511.21013401583815))
        self.assertEqual(g_algoT.TSP([5,13,26,41]),([5, 13, 25, 26, 27, 15, 39, 40, 41], 766.8152010237575))
        stop = timeit.default_timer()

        print('TSP Time: ', stop - start)


if __name__ == '__main__':
    start = timeit.default_timer()

    comperation(TestCase)
    stop = timeit.default_timer()

    print('Time: ', stop - start)
