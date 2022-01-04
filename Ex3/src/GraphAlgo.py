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
                    self._GRAPH.add_node(node["id"], node["pos"])
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
                data['Edges'].append(self.graph.edges[e])
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
            plt.plot(float(x), float(y), markersize=4, marker="o", color="red")
            # plt.text(float(x), float(y), str(n.getId), color="blue", fontsize=6)
        for e in self._GRAPH.edges.values():
            src = self._GRAPH.nodes.get(e["src"])
            dest = self._GRAPH.nodes.get(e["dest"])
            srcX = src.getPos()[0]
            srcY = src.getPos()[1]
            destX = dest.getPos()[0]
            destY = dest.getPos()[1]
            plt.annotate("", xy=(float(srcX), float(srcY)), xytext=(float(destX), float(destY)),
                         arrowprops=dict(arrowstyle="<-", edgecolor="yellow", lw=1.0))
        plt.show()

    def dijkstra(self, g: DiGraph, start: int, dest: int) -> (dict, list):
        unvisited = list(self._GRAPH.nodes.keys())
        visited = {i: float('inf') for i in unvisited}
        path = defaultdict(list)

        current = None
        # let's find the node with the lowest weight value
        for node in unvisited:
            if current == None:
                current = node
            elif visited[node] < visited[current]:
                current = node


            # if minNode is None or minNode == dest:
            #     break

            # nodes.remove(minNode)
            currentWeight = visited[current]

            neighbors = self._GRAPH.all_out_edges_of_node(current)

            for i in range(len(neighbors)):
                m = neighbors[i]
                w = m["weight"]
                value = visited[minNode] + w

                # value = currentWeight + w
                v = visited[m["other_node_id"]]
                if value < v["weight"]:
                    visited[minNode]["weight"] = value
                    path[m]["weight"] = minNode
        unvisited.remove(current)

        return visited, path
    # unvisited = list(self._GRAPH.nodes.keys())
    #
    # shortest_from_src = {i: float('inf') for i in unvisited}  # dist between src and other nodes
    # shortest_from_src[start] = 0  # dist from src to itself is 0
    #
    # previous_nodes = {}
    #
    # while unvisited:
    #     current = None
    #     # let's find the node with the lowest weight value
    #     for node in unvisited:
    #         if current == None:
    #             current = node
    #         elif shortest_from_src[node] < shortest_from_src[current]:
    #             current = node
    #
    #     neighbors = self._GRAPH.all_out_edges_of_node(current)
    #
    #     for i in range(len(neighbors)):
    #         m = list(neighbors[i])
    #         value = shortest_from_src[current] + neighbors[i].get(m[0])
    #         if value < shortest_from_src[m[1]]:
    #             shortest_from_src[m[1]] = value
    #             previous_nodes[m[1]] = current
    #
    #     unvisited.remove(current)
    #
    # return previous_nodes, shortest_from_src


if __name__ == '__main__':
    g_algo = GraphAlgo()
    file = r"C:\Users\User\PycharmProjects\pythonProject\Ex3\data\A0.json"
    g_algo.load_from_json(file)
    for n in g_algo.get_graph().nodes.values():
        if n.getPos() != None:
            x =(dict)(n.getPos())
            # y = n.getPos()[1]
            # z = n.getPos()[2]
        else:
            x = random.randrange(0, 100)
            y = random.randrange(0, 100)
            z = random.randrange(0, 100)
        print(x)
        # print(y)
        # print(z)
    # print(g_algo.get_graph())
    # g_algo.plot_graph()
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
