class Node:
    def __init__(self, label):
        self.connections = []
        self.label = label

    def add_connection(self, node, weight=None, directed=False, called_from_adj_matrix=False):
        conn = {
            'node': node,
            'weight': weight,
            'directed': directed
        }
        self.connections.append(conn)

        if not directed and not called_from_adj_matrix:
            new_conn = conn.copy()
            new_conn['node'] = self
            node.connections.append(new_conn)

    def __str__(self) -> str:
        return self.label

