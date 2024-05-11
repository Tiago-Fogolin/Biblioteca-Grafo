from graph.node import Node
from template.html_writer import HtmlWriter
from template.svg_writer import SVGWriter

def create_nodes_from_labels(size, labels):
        str_list = labels if labels else list(map(str, range(size)))
        
        return list(map(Node, str_list))
    
def create_node_dict(nodes):
    node_dict = dict(
        [(i, str(node)) for i, node in enumerate(nodes)]
    )

    return node_dict

def invert_node_dict(node_dict):
    return dict( (node_label, i) for i, node_label in node_dict.items() )

class Graph:
    """
    A class that represents a graph with nodes and its connections.
    """
    
    def __init__(self, directed=False):
        self.nodes = []
        self.directed = directed

    def add_node(self, label: str) -> None:
        """
        Args:
            label (str): Indicates the label of a new node in the graph.
        """
        new_node = Node(label)
        if str(new_node) not in list(map(str, self.nodes)):
            self.nodes.append(new_node)

    def create_connection(self, from_: str, to_: str, weight: int = 1, directed: bool = False):
        """
        Args:
            from_ (str): Indicates the label of the node it is creating the connection.
            to_ (str): Indicates the label of the node that is being connected.
            weight (int, optional): Indicates the weigth of the connection.
            directed (boolean, optional): Indicates wether the connection is directed or not.
        """
        from_node = None
        to_node = None
        for node in self.nodes:
            if node.label == from_:
                from_node = node
            if node.label == to_:
                to_node = node
            
        if not from_node or not to_node:
            raise Exception("Node not found.")
    
        from_node.add_connection(to_node, weight, directed)

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
    
    def from_adjacency_matrix(adj_matrix: list , directed: bool = False, custom_labels: list = None):
        """
        Args:
            adj_matrix (list): A list that represents the connections of the graph.
            directed (bool, optional): Indicates wether the connections are directed or not.
            custom_labels (list, optional): A list containing the labels of the nodes.
        """
        ajd_matrix_graph = Graph(directed)
        ajd_matrix_graph.nodes = create_nodes_from_labels(
            len(adj_matrix), 
            custom_labels
        )

        ajd_matrix_graph.node_dict = create_node_dict(ajd_matrix_graph.nodes)

        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                weight = adj_matrix[i][j]
                if weight != 0:
                    
                    ajd_matrix_graph.create_connection(
                        ajd_matrix_graph.node_dict[i],
                        ajd_matrix_graph.node_dict[j],
                        weight,
                        directed,
                    )
        return ajd_matrix_graph

    def generate_adjacency_matrix(self):
        matrix_size = len(self.nodes)
        adj_matrix = [[0 for i in range(matrix_size)] for i in range(matrix_size)]
        node_dict = invert_node_dict(create_node_dict(self.nodes))
        connections = self.get_connections()

        for conn in connections:
            i = node_dict[conn['from']]
            j = node_dict[conn['to']]
            adj_matrix[i][j] = conn['weight']

        return adj_matrix
    
    def get_total_weight(self):
        return sum(list(map(lambda x: x['weight'], self.get_connections())))

    def get_mean_weight(self):
        return self.get_total_weight()/len(self.get_connections())
    
    def output_html(self, file_name):
        svg_writer = SVGWriter()

        svg_writer.draw_graph(self.nodes, self.get_connections(), self.directed)

        html_writer = HtmlWriter(str(svg_writer.get_svg()))

        html_writer.output(file_name)