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
                DiGraphAlgo(self, graph)
            return True
        except IOError as er:
            print(er)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                json.dump(self, indent=4, fp=f, default=lambda a: a.__dict__)
        except IOError as er:
            print(er)
            return False

    def Dijkstra(self, g: DiGraph, start: Node, dest: Node) -> set:
        visited = {start: Node}
        path = defaultdict(list)

        nodes = set(self._GRAPH.get_all_v())

        while nodes:
            minNode = None
            for node in nodes:
                if node in visited:
                    if minNode is None:
                        minNode = node
                    elif visited[node] < visited[minNode]:
                        minNode = node
            if minNode is None:
                break

            nodes.remove(minNode)
            currentWeight = visited[minNode]

            for edge in self._GRAPH.edges[minNode]:
                weight = currentWeight + self._GRAPH.distances[(minNode, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minNode)

        return visited, path

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        super().TSP(node_lst)

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass