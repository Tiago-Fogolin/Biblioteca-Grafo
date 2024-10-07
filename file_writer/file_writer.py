class FileWriterTemplate:
    def write_file(self, path: str): raise NotImplementedError()

class NetFileWriter(FileWriterTemplate):
    
    def write_file(self, path: str, nodes, edges, arcs):
        with open(path, 'w', encoding='utf-8') as file:
            node_count = len(nodes)

            file.write(f"*vertices {node_count}\n")
            for index, node in nodes.items():
                file.write(f'{index} "{node}"\n')

            if edges:
                file.write(f"*edges\n")
                for from_, to_, weight_ in edges:
                    file.write(f"{from_} {to_} {weight_}\n")

            if arcs:
                file.write(f"*arcs\n")
                for from_, to_, weight_ in arcs:
                    file.write(f"{from_} {to_} {weight_}\n")


