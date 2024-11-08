from graph.graph import Graph
from layouts.layouts import RandomLayout, CircularLayout




grafo = Graph.from_net_file('net.net')


grafo.output_html('testenet')

