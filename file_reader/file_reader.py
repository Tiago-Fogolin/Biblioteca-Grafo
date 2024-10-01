class FileReaderTemplate:
    def read_file(self, path_to_file: str): raise NotImplementedError()

class NetFileReader(FileReaderTemplate):
    
    def read_file(self, path_to_file):
        graph_dict = {
            'nodes': [],
            'edges': [],
            'arcs': []
        }
        node_dict = {}
        with open(path_to_file, 'r', encoding='utf8') as file:
            reading_nodes = False
            reading_edges = False
            reading_arcs  = False

            for line in file.readlines():
                line = line.replace("\n", "")
                line = line.replace('"', "")

                if line.split()[0] == '*vertices':
                    reading_edges = False
                    reading_arcs  = False
                    reading_nodes = True
                    continue
                
                if line == '*edges':
                    reading_edges = True
                    reading_arcs  = False
                    reading_nodes = False
                    continue

                if line == '*arcs':
                    reading_edges = False
                    reading_arcs  = True
                    reading_nodes = False
                    continue

                if reading_nodes:
                    node_index, node_label = line.split()
                    graph_dict['nodes'].append(node_label)
                    node_dict[node_index] = node_label

                elif reading_edges:
                    from_index, to_index, weight = line.split()

                    conn = {
                        'from': node_dict[from_index],
                        'to': node_dict[to_index],
                        'weight': weight
                    }
                    
                    graph_dict['edges'].append(conn)
                
                elif reading_arcs:
                    from_index, to_index, weight = line.split()

                    conn = {
                        'from': node_dict[from_index],
                        'to': node_dict[to_index],
                        'weight': weight
                    }
                    
                    graph_dict['arcs'].append(conn)

        return graph_dict
                    
