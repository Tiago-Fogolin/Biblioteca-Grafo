import random
from functools import partial

class LayoutTemplate:

    def get_positions(self, nodes): raise NotImplementedError()

class RandomLayout(LayoutTemplate):

    def __init__(self) -> None:
        super().__init__()
        self._func_x = partial(random.randint, 20, 1500)
        self._func_y = partial(random.randint, 20, 700)
        self.positions = {}

    def generate_positions(self, nodes):
        for i, node in enumerate(nodes):
            random_x = self._func_x()
            random_y = self._func_y()
            self.positions[node.label] = {'x':random_x, 'y':random_y, 'index': i}   
        return self.positions

class CircularLayout(LayoutTemplate):

    def __init__(self) -> None:
        super().__init__()
        self.radius = 5 
        self.center_x = 800
        self.center_y = 400
        self.positions = {}

    def get_positions(self, nodes):
        for i, node in enumerate(nodes):
           ...