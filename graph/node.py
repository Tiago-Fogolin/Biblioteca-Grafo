class Node:
    """
    A class that represents a node in the graph.   
    """

    def __init__(self, label: str) -> None:
        """
        Args:
            label (str): Indicates the label of the node.
        """
        
        self.connections = []
        self.label = label

    def add_connection(self, node: 'Node', weight: int = 1, directed: bool = False) -> None:
        """
        Args:
            node (Node): The node to which a connection is added.
            weight (int, optional): The weight of the connection.
            directed (bool, optional): Indicates wheter its a directed or non directed connection.
        """

        conn = {
            'node': node,
            'weight': weight,
            'directed': directed
        }
        self.connections.append(conn)

    def __str__(self) -> str:
        return self.label

