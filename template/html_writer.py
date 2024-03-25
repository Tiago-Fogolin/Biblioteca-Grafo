class HtmlWriter:

    def __init__(self, nodes, connections):
        self.nodes = nodes
        self.connections = connections

    def __read_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
        
    def __list_to_string(self, list):
        return f"{list}"
    
    def __dict_to_string(self, dict):
        return f"{dict}"

    def output(self, file_name):
        html_string = self.__read_file('template/template.html')
        script_string = self.__read_file('template/script.js')

        node_string = self.__list_to_string(self.nodes)
        connections_string = self.__dict_to_string(self.connections)

        script_string = script_string.replace('ESCAPE_NODES', node_string)
        script_string = script_string.replace('ESCAPE_CONNECTIONS', connections_string)

        final_string = html_string.replace('EscapeScript', script_string)

        with open(file_name + '.html', 'w') as file:
            file.write(final_string)

