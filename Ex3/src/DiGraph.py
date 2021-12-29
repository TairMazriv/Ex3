from GraphInterface import GraphInterface
from Edge import Edge
from Node import Node

class DiGraph(GraphInterface):

    def __init__(self, nodes: dict, edges: dict):
        self.nodes = nodes
        self.edges = edges
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
            if e["dest"] == id1:
                a = {}
                a["other_node_id"] = e["src"]
                a["weight"] = e["w"]
                dict[len(dict)] = a
                return dict

    def all_out_edges_of_node(self, id1: int) -> dict:
        dict = {}
        for e in self.edges:
            if e["src"] == id1:
                a = {}
                a["other_node_id"] = e["dest"]
                a["weight"] = e["w"]
                dict[len(dict)] = a
        return dict

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        for e in self.edges:
            if e["src"]==id1 and e["dest"]==id2:
                return False
        self.edges[self.e_size()] = {"src":id1,"w":weight, "dest":id2}
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

if __name__ == '__main__':
    edges = [{"src":1,"w":2, "dest":2}, {"src":0,"w":2, "dest":2}]
    # , {"src": 1, "dest": 2}: Edge(1, 1, 2), {"src": 2, "dest": 0}: Edge(2, 1, 0)
    nodes = {0:Node("0,1,2", 0), 1: Node("2,3,5", 1), 2: Node("0.3,2,1",2)}
    d = DiGraph(nodes, edges)
    d.add_edge(0,1,3)
    print(d)
    # print(d.e_size())