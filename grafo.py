from graph.graph import Graph

grafo = Graph()
matriz_adjacencia = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]


grafo.create_from_adj_matrix(matriz_adjacencia, directed=True, custom_labels=['zero','um', 'dois', 'tres', 'quatro', 'cinco'])

grafo.output_html('teste')
for item in grafo.generate_adj_matrix():
    print(item, end= '\n')

print()

for conn in grafo.get_connections():
    print(conn, end= '\n')