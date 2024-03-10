class Node:
    def __init__(self, label):
        self.connections = []
        self.label = label

    def add_connection(self, node, weight=None, bidirectional=False):
        conn = {
            'node': node,
            'weight': weight
        }
        self.connections.append(conn)

        if bidirectional:
            node.add_connection(self, weight)

    def __str__(self) -> str:
        return self.label


class Graph:
    
    def __init__(self):
        self.nodes = []

    def add_node(self, label):
        new_node = Node(label)
        if new_node not in self.nodes:
            self.nodes.append(new_node)

    def create_connection(self, from_, to_, weight=None, bidirectional=False):
        from_node = None
        to_node = None
        for node in self.nodes:
            if node.label == from_:
                from_node = node
            elif node.label == to_:
                to_node = node
            
        if not from_node or not to_node:
            raise Exception("Node not found.")
    
        from_node.add_connection(to_node, weight, bidirectional)

    def get_connections(self):
        all_connections = []
        
        for node in self.nodes:
            formatted_conn = {}

            for conn in node.connections:

                formatted_conn['from'] = str(node)
                formatted_conn['to'] = str(conn['node'])
                formatted_conn['weight'] = conn['weight']
                
                all_connections.append(formatted_conn)

        return all_connections

        

gra = Graph()
gra.add_node('teste')
gra.add_node('teste2')

gra.create_connection('teste', 'teste2', weight=1, bidirectional=True)

for conn in gra.get_connections():
    print(conn, end= '\n')

