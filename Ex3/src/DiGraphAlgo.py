import json
import sys
from typing import List
import threading, queue
from DiGraph import DiGraph
import GraphInterface, Node
from GraphAlgoInterface import GraphAlgoInterface


class DiGraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph):
        self._GRAPH = g;

    def get_graph(self) -> GraphInterface:
        return self._GRAPH

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as fn:
                load = json.load(fn)
                graph = DiGraph()
                for node in load["Nodes"]:
                    graph.add_node(node["id"], node["pos"])
                for edge in load["Edges"]:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])
                return graph
        except IOError as er:
            print(er)

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass