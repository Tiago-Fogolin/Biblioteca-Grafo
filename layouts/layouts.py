import random
from functools import partial
import math

MAX_WIDTH = 1500
MIN_WIDTH = 20
MAX_HEIGHT = 700
MIN_HEIGHT = 20

 
def denormalize_positions(normalized_positions):
    denormalized_positions = {}

    x_center_offset = (MAX_WIDTH - MIN_WIDTH) / 2
    y_center_offset = (MAX_HEIGHT - MIN_HEIGHT) / 2

    for node_label, node_position in normalized_positions.items():
        new_x = float(node_position['x']) * (MAX_WIDTH - MIN_WIDTH) + MIN_WIDTH
        new_y = float(node_position['y']) * (MAX_HEIGHT - MIN_HEIGHT) + MIN_HEIGHT
        denormalized_positions[node_label] = {'x': new_x, 'y': new_y, 'index': node_position['index']}

    return denormalized_positions

def normalize_positions(denormalized_positions):
    normalized_positions = {}

    for node_label, node_position in denormalized_positions.items():
        new_x =  (float(node_position['x']) - MIN_WIDTH) / (MAX_WIDTH - MIN_WIDTH)
        new_y = (float(node_position['y']) - MIN_HEIGHT) / (MAX_HEIGHT - MIN_HEIGHT)
        normalized_positions[node_label] = {'x': new_x, 'y': new_y, 'index': node_position['index']}
        
    return normalized_positions

class LayoutTemplate:

    def generate_positions(self, nodes): raise NotImplementedError()

class RandomLayout(LayoutTemplate):

    def __init__(self) -> None:
        super().__init__()
        self._func_x = partial(random.randint, MIN_WIDTH, MAX_WIDTH)
        self._func_y = partial(random.randint, MIN_HEIGHT, MAX_HEIGHT)
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
        self.radius = 200
        self.angle = 90
        self.center_x = 800
        self.center_y = 400
        self.positions = {}

    def generate_positions(self, nodes):
        next_mirrored = False
        visited_positions = set()
        quadrants = [(1,1), (1,-1), (-1,-1), (-1,1)]
        quadrant_index = 0

        for i, node in enumerate(nodes):
            while True:
                x_sign = quadrants[quadrant_index][0]
                y_sign = quadrants[quadrant_index][1]

                next_pos = [self.radius*math.cos(math.radians(self.angle)), self.radius*math.sin(math.radians(self.angle))]
                
                if next_mirrored:
                    next_pos[0], next_pos[1] = next_pos[1], next_pos[0]

                next_x = x_sign * next_pos[0] + self.center_x
                next_y = y_sign * next_pos[1] + self.center_y

                if (next_x, next_y) not in visited_positions:
                    break

                quadrant_index += 1

                if quadrant_index == 4:
                    quadrant_index = 0

                    if not next_mirrored:
                        if (next_pos[0], next_pos[1]) != (next_pos[1], next_pos[0]):
                            next_mirrored = True
                            continue

                    if next_mirrored:
                        next_mirrored = False

                    self.angle /= 2
                

            visited_positions.add((next_x, next_y))

            self.positions[node.label] = {'x': next_x, 'y': next_y, 'index': i}

           
       
        return self.positions