import sys
from typing import List
import threading, queue
from DiGraph import DiGraph
from src import GraphInterface, Node
from src.GraphAlgoInterface import GraphAlgoInterface


class DiGraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph):
        self._GRAPH = g;

    def get_graph(self) -> GraphInterface:
        return self._GRAPH

    def load_from_json(self, file_name: str) -> bool:
        pass

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
