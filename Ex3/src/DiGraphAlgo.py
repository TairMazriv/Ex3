import json
import sys
from collections import defaultdict
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

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        a = dijkstra(self._GRAPH, id1, id2)
        visited = a[0]
        path = a[1]
        ans = []
        ansdist = 0
        for x in visited:
            ans.append(visited.get(x))

        for x in path:
            ansdist += path.get(x)

        return (ansdist, ans)

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        citiesdata = []
        result = []
        same, place = 0, 0
        for i in range(len(node_lst)):
            citiesdata.append(node_lst[i])

        list = []
        temp = node_lst[0]
        result.append(self._GRAPH.nodes.get(citiesdata.pop(0)))
        while len(citiesdata) >= 1:
            min = sys.Max_Value
            same = -1
            place = -1
            for i in range(len(citiesdata)):
                open = citiesdata[i]
                if self.shortest_path(temp, open)[0] < min:
                    min = self.shortest_path(temp, open)[0]
                    same = open
                    place = i
            list = self.shortest_path(temp, same)[1]
            while len(list) >= 1:
                if list[0] not in result:
                    result.append(list[0])
                list.remove(0)
            q = citiesdata[place]
            temp = self._GRAPH.nodes.get(q)
            citiesdata.remove(citiesdata[place])
            if len(citiesdata) == 1 and self._GRAPH.nodes.get(same + 1) not in result:
                result.append(self._GRAPH.nodes.get(same + 1))
        return result

    def centerPoint(self) -> (int, float):
        super().centerPoint()

    def plot_graph(self) -> None:
        pass


def dijkstra(self, g: DiGraph, start: int, dest: int) -> (dict, list):
    visited = {start: int}
    path = defaultdict(list)

    nodes = set(g.get_all_v())

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None or minNode == dest:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in g.edges[minNode]:
            weight = currentWeight + g.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path
