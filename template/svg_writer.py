import svg
import random


class SVGWriter:

    def __init__(self) -> None:
        self.elements = []
        self.centers  = {}
        self.set_default_settings()

    def set_default_settings(self):
        self.node_color = 'blue'

    def add_node(self, x, y, label, node_index):
        self.elements.append(
            svg.Circle(
                cx=x,
                cy=y,
                stroke=self.node_color,
                fill=self.node_color,
                r=20,
                class_=f'node{node_index}'
            )
        )
        self.add_label(x, y+35, label, node_index)

    def add_label(self, x, y, label, node_index):
        self.elements.append(
            svg.Text(
                text=label,
                text_anchor='middle',
                x=x,
                y=y,
                class_=f'label{node_index}'
            )
        )

    def add_line(self, x1, y1, x2, y2, from_index, to_index):
        self.elements.append(
            svg.Line(
                x1=x1,
                y1=y1,
                x2=x2,
                y2=y2,
                stroke='black',
                class_=f'{from_index}line{to_index}',
                marker_end='url(#arrow)'
            )
        )

    def add_arrow_ref(self):
        arrow_head = svg.Path(
            d='M0,0 L0,6 L9,3 z',
            fill='black'
        )

        arrow_marker = svg.Marker(
            id='arrow',
            markerWidth='30',
            markerHeight='30',
            refX='29',
            refY='3',
            orient='auto',
            markerUnits='strokeWidth',
            elements=[arrow_head]
        )

        defs = svg.Defs(
            elements=[arrow_marker]
        )

        self.elements.append(defs)

    def draw_graph(self, nodes, connections, directed):
        self.generate_node_positions(nodes)
        if directed:
            self.add_arrow_ref()

        self.draw_lines(connections)
        self.draw_nodes(nodes)

    def generate_node_positions(self, nodes):
        for i, node in enumerate(nodes):
            random_x = random.randint(20, 600)
            random_y = random.randint(20, 600)
            self.centers[node.label] = {'x':random_x, 'y':random_y, 'index': i}

    def draw_nodes(self, nodes):
        for node in nodes:
            self.add_node(
                x=self.centers[node.label]['x'],
                y=self.centers[node.label]['y'],
                label=node.label,
                node_index=self.centers[node.label]['index']
            )

    def draw_lines(self, connections):
        for conn in connections:
            from_node = conn['from']
            to_node = conn['to']
            self.add_line(
                x1=self.centers[from_node]['x'],
                y1=self.centers[from_node]['y'],
                x2=self.centers[to_node]['x'],
                y2=self.centers[to_node]['y'],
                from_index=self.centers[from_node]['index'],
                to_index=self.centers[to_node]['index']
            )

    def get_svg(self):
        return svg.SVG(
            elements=self.elements
        )
