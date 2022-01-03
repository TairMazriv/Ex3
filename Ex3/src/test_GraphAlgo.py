from unittest import TestCase
from src import DiGraph, GraphAlgo
from  GraphAlgo import GraphAlgo
import json


g_algo = GraphAlgo()
file = r"C:\Users\tairm\PycharmProjects\Ex3\src\A0.json"
class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        self.assertEqual(g_algo._GRAPH, g_algo.get_graph())

    def test_load_from_json(self):
        self.assertTrue(g_algo.load_from_json(file))

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        self.fail()

    def test_plot_graph(self):
        self.fail()
