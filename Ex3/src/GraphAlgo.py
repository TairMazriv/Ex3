import json
import sys
from collections import defaultdict
from typing import List
import threading, queue
import DiGraph, GraphInterface, GraphAlgoInterface, Node, Edge
from DiGraph import DiGraph
import GraphInterface, Node
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from Node import Node
import random
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g=DiGraph()):
        self._GRAPH = g

    def __str__(self):
        return f"graph:{self._GRAPH}"

    def __repr__(self):
        return f"graph:{self._GRAPH}"

    def get_graph(self) -> GraphInterface:
        return self._GRAPH

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as fn:
                load = json.load(fn)
                # graph = DiGraph()
                for node in load["Nodes"]:
                    pos = (node["pos"]).split(',')
                    self._GRAPH.add_node(node["id"], pos)
                for edge in load["Edges"]:
                    self._GRAPH.add_edge(edge["src"], edge["dest"], edge["w"])
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
            for e in self._GRAPH.edges:
                data['Edges'].append(self._GRAPH.edges[e])
            for n in self._GRAPH.nodes:
                node = {'pos': self._GRAPH.nodes[n].pos, 'id': self._GRAPH.nodes[n].id}
                data['Nodes'].append(node)
            print(data)
            with open(file_name, 'w') as outfile:
                json.dump(data, outfile)
        except IOError as er:
            print(er)
            return False

        def shortest_path(self, id1: int, id2: int) -> (float, list):
        a = self.dijkstra(id1, id2)
        visited = a[0]
        path = a[1]
        # if there is no path
        if visited.get(id2) == float('inf'):
            return float('inf'), []
        ans = []

        node = id2

        while node != id1:
            ans.append(node)
            node = visited.get(node)

        ans.append(id1)
        result = ans[::-1]

        return a[0][id2], result

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
        for n in self._GRAPH.nodes.values():
            if n.getPos() != None:
                x = n.getPos()[0]
                y = n.getPos()[1]
                z = n.getPos()[2]
            else:
                x = random.randrange(0, 100)
                y = random.randrange(0, 100)
                z = random.randrange(0, 100)
                n.setPos((x, y, z))
            plt.plot(float(x), float(y), markersize=4, marker="o", color="black")
            plt.text(float(x), float(y), n.getId(), color="blue", fontsize=8)
        for e in self._GRAPH.edges.values():
            src = self._GRAPH.nodes.get(e["src"])
            dest = self._GRAPH.nodes.get(e["dest"])
            srcX = src.getPos()[0]
            srcY = src.getPos()[1]
            destX = dest.getPos()[0]
            destY = dest.getPos()[1]
            plt.annotate("", xy=(float(srcX), float(srcY)), xytext=(float(destX), float(destY)),
                         arrowprops=dict(arrowstyle="-", edgecolor="black", lw=1.0))
        plt.show()

       def dijkstra(self, start: int, dest: int) -> (dict, list):
        unvisited = list(self._GRAPH.nodes.keys())
        visited = {i: float('inf') for i in unvisited}
        path = {}
        visited[start] = 0
        while unvisited:
            minNode = None
        # let's find the node with the lowest weight value
            for node in unvisited:
                if minNode == None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node

            neighbors = self._GRAPH.all_out_edges_of_node(minNode)

            for i in range(len(neighbors)):
                m = neighbors[i]
                w = m["weight"]
                value = visited[minNode] + w
                oni = m["other_node_id"]
                if value < visited[oni]:
                    visited[oni] = value
                    visited[oni] = minNode

            unvisited.remove(minNode)

        return visited, path


if __name__ == '__main__':
    g_algo = GraphAlgo()
    file = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A5.json"
    g_algo.load_from_json(file)
    print(g_algo.get_graph())
    # edges = [{"src": 0, "w": 1, "dest": 1}, {"src": 1, "w": 2, "dest": 4}]
    # , {"src": 1, "dest": 2}: Edge(1, 1, 2), {"src": 2, "dest": 0}: Edge(2, 1, 0)
    # nodes = {0: Node("0,1,2", 0), 1: Node("2,3,5", 1), 2: Node("0.3,2,1", 2)}
# d = DiGraph(nodes, edges)
# print(d)
# g_algo = GraphAlgo(d)
# g_algo.addNode(0)
# g_algo.addNode(1)
# g_algo.addNode(2)
# g_algo.addEdge(0, 1, 1)
# g_algo.addEdge(1, 2, 4)
# print(g_algo.dijkstra(d,1, 2))
# g_algo.shortest_path()
# #        (1, [0, 1])
# #        >>> g_algo.shortestPath(0,2)
# #        (5, [0, 1, 2])
