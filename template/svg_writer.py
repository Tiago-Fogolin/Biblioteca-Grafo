import svg
import random


class SVGWriter:

    def __init__(self) -> None:
        self.elements = []
        self.centers  = {}
        self.set_default_settings()

    def set_default_settings(self):
        self.node_color = 'blue'

    def add_node(self, x, y, label):
        self.elements.append(
            svg.Circle(
                cx=x,
                cy=y,
                stroke=self.node_color,
                fill=self.node_color,
                r=20
            )
        )
        self.add_label(x, y+35, label)

    def add_label(self, x, y, label):
        self.elements.append(
            svg.Text(
                text=label,
                text_anchor='middle',
                x=x,
                y=y
            )
        )

    def add_line(self, x1, y1, x2, y2):
        self.elements.append(
            svg.Line(
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2,
                stroke='black'
            )
        )

    def draw_graph(self, nodes, connections):
        self.generate_node_positions(nodes)
        self.draw_lines(connections)
        self.draw_nodes(nodes)

    def generate_node_positions(self, nodes):
        for node in nodes:
            random_x = random.randint(20, 600)
            random_y = random.randint(20, 600)
            self.centers[node.label] = [random_x, random_y]

    def draw_nodes(self, nodes):
        for node in nodes:
            self.add_node(
                x=self.centers[node.label][0],
                y=self.centers[node.label][1],
                label=node.label
            )

    def draw_lines(self, connections):
        for conn in connections:
            from_node = conn['from']
            to_node = conn['to']
            self.add_line(
                x1=self.centers[from_node][0],
                y1=self.centers[from_node][1],
                x2=self.centers[to_node][0],
                y2=self.centers[to_node][1]
            )

    def get_svg(self):
        return svg.SVG(
            elements=self.elements
        )
