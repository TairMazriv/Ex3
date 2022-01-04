from unittest import TestCase
import DiGraph, GraphAlgo, GraphInterface, GraphAlgoInterface, Node, Edge
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node import Node

class comperation(TestCase):

    def test_load_from_json(self):
        file1 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A1.json"
        g_algo1 = GraphAlgo()
        self.assertTrue(g_algo1.load_from_json(file1))

        file4 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A4.json"
        g_algo4 = GraphAlgo()
        self.assertTrue(g_algo4.load_from_json(file4))

        fileT = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\T0.json"
        g_algoT = GraphAlgo()
        self.assertTrue(g_algoT.load_from_json(fileT))

    def test_save_to_json(self):
        file1 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        self.assertTrue(g_algo1.save_to_json('A1_new'))

        file4 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        self.assertTrue(g_algo4.save_to_json('A4_new'))

        fileT = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\T0.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        self.assertTrue(g_algoT.save_to_json('T0_new'))

    def test_shortest_path(self):
        file1 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        self.assertEqual(g_algo1.shortest_path(0,8), (7.436808665895908, [0, 1, 2, 6, 7, 8]))
        self.assertEqual(g_algo1.shortest_path(5,16), (8.335654448747263, [5, 6, 2, 1, 0, 16]))

        file4 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        self.assertEqual(g_algo4.shortest_path(11,23), (10.059226856826783, [11, 12, 13, 14, 17, 16, 0, 22, 23]))
        self.assertEqual(g_algo4.shortest_path(1,39), (9.589550839925723, [1, 2, 6, 7, 8, 9, 10, 39]))

        fileT = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\T0.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        self.assertEqual(g_algoT.shortest_path(0, 3), (3.032037506070033, [0, 1, 3]))
        self.assertEqual(g_algoT.shortest_path(1, 2), (1.8015954015822042, [1, 2]))

    def test_centerPoint(self):
        file1 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        ans1, min1 = 8, 9.925289024973141
        self.assertEqual(g_algo1.centerPoint(), (ans1, min1))

        file4 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        ans4, min4 = 6, 7.597344259985743
        self.assertEqual(g_algo4.centerPoint(), (ans4, min4))

        fileT = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\T0.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        ansT, minT = 6, 7.597344259985743
        self.assertEqual(g_algoT.centerPoint(), (ansT, minT))

    def test_TSP(self):
        file1 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        ans1, min1 = 8, 9.925289024973141
        self.assertEqual(g_algo1.centerPoint(), (ans1, min1))

        file4 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        ans4, min4 = 6, 7.597344259985743
        self.assertEqual(g_algo4.centerPoint(), (ans4, min4))

        fileT = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\T0.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        ansT, minT = 6, 7.597344259985743
        self.assertEqual(g_algoT.centerPoint(), (ansT, minT))