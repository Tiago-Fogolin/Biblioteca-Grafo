from graph.graph import Graph
from layouts.layouts import RandomLayout, CircularLayout




grafo = Graph.from_net_file('testenet.txt')


grafo.output_net_file('outputnet.txt')
