from GraphInterface import GraphInterface
from Edge import Edge
from Node import Node

class DiGraph(GraphInterface):

    def __init__(self, nodes: dict, edges: dict):
        self.nodes = nodes
        self.edges = edges
        self.mc = 0

    def v_size(self) -> int:
        return self.nodes.size

    def e_size(self) -> int:
        return self.edges.size

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        dict = {}
        for key in self.edges.keys():
            if id1 == key["src"]:
                dict["dest"] = self.edges(key)
        return dict

    def all_out_edges_of_node(self, id1: int) -> dict:
        dict = {}
        for key in self.edges.keys():
            if id1 == key["dest"]:
                dict["src"] = self.edges(key)
        return dict

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if {"src": id1,"dest": id2} in self.edges.keys():
            return False
        else:
            self.edges[{"src": id1,"dest": id2}] = Edge(id1, id2, weight)
            self.mc += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = Node(node_id, pos)
            self.mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            self.nodes.pop(node_id)
            for key in self.edges.keys():
                if node_id in key:
                    self.edges.pop(key)
            self.mc +=1
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if {"src": node_id1, "dest": node_id2} in self.edges.keys():
            self.edges.pop({"src": node_id1, "dest": node_id2})
            self.mc += 1
            return True
        else:
            return False
