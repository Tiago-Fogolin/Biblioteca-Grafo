from node import Node
from html_writer import HtmlWriter

class Graph:
    
    def __init__(self):
        self.nodes = []

    def add_node(self, label):
        new_node = Node(label)
        if new_node not in self.nodes:
            self.nodes.append(new_node)

    def create_connection(self, from_, to_, weight=None, directed=False, called_from_adj_matrix=False):
        from_node = None
        to_node = None
        for node in self.nodes:
            if node.label == from_:
                from_node = node
            if node.label == to_:
                to_node = node
            
        if not from_node or not to_node:
            raise Exception("Node not found.")
    
        from_node.add_connection(to_node, weight, directed, called_from_adj_matrix)

    def get_connections(self):
        all_connections = []
        
        for node in self.nodes:
            
            for conn in node.connections:
                formatted_conn = {}

                formatted_conn['from'] = str(node)
                formatted_conn['to'] = str(conn['node'])
                formatted_conn['weight'] = conn['weight']
                
                all_connections.append(formatted_conn)

        return all_connections
    
    def create_from_adj_matrix(self, adj_matrix, directed=False,custom_labels=None):
        self.nodes = self.__create_nodes_from_labels(
            len(adj_matrix), 
            custom_labels
        )

        self.node_dict = self.__create_node_dict()

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                weight = adj_matrix[i][j]
                if weight != 0:
                    
                    self.create_connection(
                        self.node_dict[i],
                        self.node_dict[j],
                        weight,
                        directed,
                        called_from_adj_matrix=True
                    )

    def generate_adj_matrix(self):
        matrix_size = len(self.nodes)
        adj_matrix = [[0 for i in range(matrix_size)] for i in range(matrix_size)]
        node_dict = self.__invert_node_dict(self.__create_node_dict())
        connections = self.get_connections()

        for conn in connections:
            i = node_dict[conn['from']]
            j = node_dict[conn['to']]
            adj_matrix[i][j] = conn['weight']

        return adj_matrix
    
    def output_html(self, file_name):
        html_writer = HtmlWriter(list(map(str, self.nodes)), self.get_connections())

        html_writer.output(file_name)

    def __create_nodes_from_labels(self, size, labels):
        if labels:
            return list(map(Node, labels))
    
        str_range = list(map(str, range(size)))
        return list(map(Node, str_range))
    
    def __create_node_dict(self):
        node_dict = dict(
            [(i, str(node)) for i, node in enumerate(self.nodes)]
        )

        return node_dict

    def __invert_node_dict(self, node_dict):
        return dict( (node_label, i) for i, node_label in node_dict.items() )


grafo = Graph()
matriz_adjacencia = [
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

grafo.create_from_adj_matrix(matriz_adjacencia, directed=True, custom_labels=['zero','um', 'dois', 'tres', 'quatro'])

for item in grafo.generate_adj_matrix():
    print(item, end= '\n')

print()

for conn in grafo.get_connections():
    print(conn, end= '\n')

grafo.output_html('teste')