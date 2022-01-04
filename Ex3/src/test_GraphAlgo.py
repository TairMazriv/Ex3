from unittest import TestCase
from src import DiGraph, GraphAlgo
from  GraphAlgo import GraphAlgo
import json


g_algo = GraphAlgo()
file = r"C:\Users\tairm\PycharmProjects\Ex3\src\A1.json"
class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.assertEqual(g_algo._GRAPH, g_algo.get_graph())

    def test_load_from_json(self):
        self.assertTrue(g_algo.load_from_json(file))

    def test_save_to_json(self):
        # self.fail()
        self.assertTrue(g_algo.save_to_json('saved_'+r"C:\Users\tairm\PycharmProjects\Ex3\src\A0.json"))


    def test_shortest_path(self):
        g1_algo = GraphAlgo()
        file = r"C:\Users\tairm\PycharmProjects\Ex3\src\A0.json"
        g1_algo.load_from_json(file)
        dist, path = g1_algo.shortest_path(0,1)
        self.assertEqual(g1_algo.shortest_path(0,1), (dist, path))
        # self.fail()

    def test_tsp(self):
        g_algo = GraphAlgo()
        file = r"C:\Users\tairm\PycharmProjects\Ex3\src\A3.json"
        g_algo.load_from_json(file)
        result, answer = (
        [0, 21, 22, 23, 24, 25, 26, 8, 7, 44, 43, 42, 41, 40, 39, 17, 14, 15, 38, 37, 36, 35, 34, 33, 32, 2, 3, 31, 30,
         13, 12, 11, 20, 19, 18, 10, 9, 1, 16, 6, 5, 28, 4, 29, 48, 47, 46, 45, 46, 27], 8459.737919535499)

        self.assertEqual(g_algo.TSP(g_algo.get_graph().nodes), (result, answer))

    def test_centerPoint(self):
        g_algo = GraphAlgo()
        file = r"C:\Users\tairm\PycharmProjects\Ex3\src\A0.json"
        g_algo.load_from_json(file)
        node, min= 7, 6.806805834715163
        self.assertEqual(g_algo.centerPoint(), (node, min))
