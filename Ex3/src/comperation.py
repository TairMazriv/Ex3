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

    # def test_shortest_path(self):

    def test_centerPoint(self):
        file1 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A1.json"
        g_algo1 = GraphAlgo()
        g_algo1.load_from_json(file1)
        ans1, min1 = 0, 2.2250738585072014e-308
        self.assertEqual(g_algo1.centerPoint(), (ans1, min1))

        file4 = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A4.json"
        g_algo4 = GraphAlgo()
        g_algo4.load_from_json(file4)
        ans4, min4 = 0, 2.2250738585072014e-308
        self.assertEqual(g_algo4.centerPoint(), (ans4, min4))

        fileT = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\T0.json"
        g_algoT = GraphAlgo()
        g_algoT.load_from_json(fileT)
        ansT, minT = 0, 2.2250738585072014e-308
        self.assertEqual(g_algoT.centerPoint(), (ansT, minT))
