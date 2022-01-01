from GraphInterface import GraphInterface
from Edge import Edge
from Node import Node

class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def __str__(self):
        return f"nodes:{self.nodes} , edges:{self.edges}"

    def __repr__(self):
        return f"nodes:{self.nodes} , edges:{self.edges}"

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def get_all_e(self) -> dict:
        return self.edges

    def all_in_edges_of_node(self, id1: int) -> dict:
        dict = {}
        for e in self.edges:
            if self.edges[e]["dest"] == id1:
                dict[len(dict)] = {"other_node_id": self.edges[e]["src"], "weight": self.edges[e]["w"]}
        return dict

    def all_out_edges_of_node(self, id1: int) -> dict:
        dict = {}
        for e in self.edges:
            if self.edges[e]["src"] == id1:
                dict[len(dict)] = {"other_node_id": self.edges[e]["dest"], "weight": self.edges[e]["w"]}
        return dict

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        for e in self.edges:
            if self.edges[e]["src"]==id1 and self.edges[e]["dest"]==id2:
                return False
        self.edges[self.e_size()] = {"src":id1,"w":weight, "dest":id2}
        self.mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes.keys():
            return False
        else:
            self.nodes[node_id] = Node(pos,node_id)
            self.mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            self.nodes.pop(node_id)
            for e in self.edges:
                if node_id==self.edges[e]["src"] or node_id==self.edges[e]["dest"]:
                    del self.edges[e]
                self.mc +=1
                return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        for e in self.edges:
            if self.edges[e]["src"]==node_id1 and self.edges[e]["dest"]==node_id2:
                self.edges.pop(e)
                self.mc += 1
                return True
        else:
            return False
