import unittest
from DiGraph import DiGraph

class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        self.assertEqual(g.v_size(), 4)

    def test_e_size(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(g.e_size(), 5)

    def test_get_all_v(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEquals(g.get_all_v(), g.nodes)

    def test_get_mc(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEquals(g.get_mc(), 9)

    def test_add_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        self.assertEqual(g.v_size(), 7)

    def test_add_edge(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_node(5)
        g.add_node(6)
        g.add_edge(5, 6, 4)
        g.add_edge(1, 6, 3)
        self.assertEqual(g.e_size(), 6)

    def test_remove_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.remove_node(2)
        g.remove_node(3)
        self.assertEqual(g.v_size(), 2)

    def test_remove_edge(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(2, 3)
        g.remove_edge(1, 0)
        self.assertEqual(g.e_size(), 3)

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.add_edge(2, 1, 4)
        ans = {0: {'other_node_id': 0, 'weight': 1}, 1: {'other_node_id': 2, 'weight': 4}}
        self.assertEquals(ans, g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        ans = {0: {'other_node_id': 0, 'weight': 1.1}, 1: {'other_node_id': 2, 'weight': 1.3}, 2: {'other_node_id': 3, 'weight': 1.9}}
        self.assertEquals(ans, g.all_out_edges_of_node(1))


if __name__ == '__main__':
    unittest.main()