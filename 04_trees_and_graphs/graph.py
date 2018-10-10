# -*- coding: utf-8 -*-
import unittest


class GraphNode:

    def __init__(self, name, links=None):
        self.name = name
        self.links = links if links else []


class Graph:

    def __init__(self, adjacency_list=None):
        self.nodes = []

        if not adjacency_list:
            return

        node_mapping = {}

        for name in adjacency_list:
            node = GraphNode(name)
            node_mapping[name] = node
            self.nodes.append(node)

        for node in self.nodes:
            node.links = [node_mapping[n] for n in adjacency_list[node.name]]


class TestGraphNode(unittest.TestCase):

    def test_init(self):
        n1 = GraphNode(1)
        n2 = GraphNode(2, [])
        n3 = GraphNode(3, [n1])
        n4 = GraphNode(4, [n1, n2, n3])

        self.assertEqual(n1.name, 1)
        self.assertEqual(n2.name, 2)
        self.assertEqual(n3.name, 3)
        self.assertEqual(n4.name, 4)

        self.assertEqual(n1.links, [])
        self.assertEqual(n2.links, [])
        self.assertEqual(n3.links, [n1])
        self.assertEqual(n4.links, [n1, n2, n3])


class TestGraph(unittest.TestCase):

    def test_init(self):
        adjacency_list = {
            0: [1, 2, 3],
            1: [4, 5],
            2: [],
            3: [0, 1, 2, 4, 5],
            4: [5],
            5: [0, 2, 4]
        }

        g = Graph()
        self.assertEqual(g.nodes, [])

        g = Graph(adjacency_list)
        self.assertEqual(len(g.nodes), 6)

        for node in g.nodes:
            linked_node_names = []
            for linked_node in node.links:
                linked_node_names.append(linked_node.name)
            self.assertEqual(sorted(linked_node_names), adjacency_list[node.name])
