class Node:
    def __init__(self, label):
        self.connections = []
        self.label = label

    def add_connection(self, node, weight=None, directed=False):
        conn = {
            'node': node,
            'weight': weight,
            'directed': directed
        }
        self.connections.append(conn)

        if not directed:
            new_conn = conn.copy()
            new_conn['node'] = self
            node.connections.append(new_conn)

    def __str__(self) -> str:
        return self.label


class Graph:
    
    def __init__(self):
        self.nodes = []

    def add_node(self, label):
        new_node = Node(label)
        if new_node not in self.nodes:
            self.nodes.append(new_node)

    def create_connection(self, from_, to_, weight=None, directed=False):
        from_node = None
        to_node = None
        for node in self.nodes:
            if node.label == from_:
                from_node = node
            elif node.label == to_:
                to_node = node
            
        if not from_node or not to_node:
            raise Exception("Node not found.")
    
        from_node.add_connection(to_node, weight, directed)

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

gra.create_connection('teste', 'teste2', weight=1, directed=False)

for conn in gra.get_connections():
    print(conn, end= '\n')

