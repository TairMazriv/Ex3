import json
import sys
from collections import defaultdict
from typing import List
import threading, queue
from src import DiGraph, GraphInterface, GraphAlgoInterface, Node, Edge
from DiGraph import DiGraph
import GraphInterface, Node
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from Node import Node


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g=DiGraph()):
        self.graph = DiGraph()

    def __str__(self):
        return f"graph:{self.graph}"

    def __repr__(self):
        return f"graph:{self.graph}"

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as fn:
                load = json.load(fn)
                # graph = DiGraph()
                for node in load["Nodes"]:
                    self.graph.add_node(node["id"], node["pos"])
                for edge in load["Edges"]:
                    self.graph.add_edge(edge["src"], edge["dest"], edge["w"])
                # GraphAlgo(self, graph)
            return True
        except IOError as er:
            print(er)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            data = {}
            data['Edges'] = []
            data['Nodes'] = []
            for e in self.graph.edges:
                data['Edges'].append(self.graph.edges[e])
            for n in self.graph.nodes:
                node = {'pos': self.graph.nodes[n].pos, 'id': self.graph.nodes[n].id}
                data['Nodes'].append(node)
            print(data)
            with open(file_name, 'w') as outfile:
                json.dump(data, outfile)
        except IOError as er:
            print(er)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        a = self.dijkstra(self._GRAPH, id1, id2)
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
            min = sys.Maxint
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
        min = sys.float_info.max
        max = sys.float_info.min
        ans = 0
        for i in range(len(self._GRAPH.nodes)):
            for j in range(len(self._GRAPH.nodes)):
                if j != i:
                    temp = self.shortest_path(j, i)[0]
                    if temp > max:
                        max = temp
            center = max
            if center < min:
                min = center
                ans = self._GRAPH.nodes[i]
        return (ans, min)

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

            for edge in range(len(g.all_out_edges_of_node(minNode))):
                weight = currentWeight + g.all_out_edges_of_node(minNode).get(edge)
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge].append(minNode)

        return visited, path


if __name__ == '__main__':
    edges = [{"src": 0, "w": 1, "dest": 1}, {"src": 1, "w": 2, "dest": 4}]
    # , {"src": 1, "dest": 2}: Edge(1, 1, 2), {"src": 2, "dest": 0}: Edge(2, 1, 0)
    nodes = {0: Node("0,1,2", 0), 1: Node("2,3,5", 1), 2: Node("0.3,2,1", 2)}
d = DiGraph(nodes, edges)
print(d)
g_algo = GraphAlgo(d)
# g_algo.addNode(0)
# g_algo.addNode(1)
# g_algo.addNode(2)
# g_algo.addEdge(0, 1, 1)
# g_algo.addEdge(1, 2, 4)
g_algo.shortest_path(1, 2)
# #        (1, [0, 1])
# #        >>> g_algo.shortestPath(0,2)
# #        (5, [0, 1, 2])
