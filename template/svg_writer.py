import svg
import random


class SVGWriter:

    def __init__(self) -> None:
        self.elements = []
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
        self.add_label(x, y+30, label)

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
                y2=y2
            )
        )

    def draw_graph(self, nodes, connections=None):
        self.draw_nodes(nodes)

    def draw_nodes(self, nodes):
        for node in nodes:
            self.add_node(
                random.randint(20, 500),
                random.randint(20, 500),
                node.label
            )

    def get_svg(self):
        return svg.SVG(
            elements=self.elements
        )
