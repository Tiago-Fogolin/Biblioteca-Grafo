from unittest import TestCase
from graph.node import Node
from graph.graph import Graph

class NodeTest(TestCase):
    
    def test_add_connection(self):
        node1 = Node('node1')
        node2 = Node('node2')

        node1.add_connection('node2', weight=1, directed=False)
        connection = node1.connections[0]
        self.assertEqual(1,len(node1.connections))
        self.assertEqual({'node':'node2', 'weight': 1, 'directed': False}, connection)

class GraphTest(TestCase):

    def test_create_graph(self):
        graph = Graph()
        self.assertIsInstance(graph, Graph)

    def test_add_node(self):
        graph = Graph()
        graph.add_node('new_node')
        self.assertEqual(1, len(graph.nodes))
        self.assertEqual('new_node', graph.nodes[0].label)

        graph.add_node('new_new_node')
        self.assertEqual(2, len(graph.nodes))
        self.assertEqual('new_new_node', graph.nodes[1].label)


    def test_repeat_node(self):
        graph = Graph()
        graph.add_node('new_node')
        graph.add_node('new_node')
        self.assertEqual(1, len(graph.nodes))
        self.assertEqual('new_node', graph.nodes[0].label)


        