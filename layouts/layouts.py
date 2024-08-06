import random
from functools import partial
import math

class LayoutTemplate:

    def generate_positions(self, nodes): raise NotImplementedError()

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
        self.radius = 200
        self.angle = 90
        self.center_x = 800
        self.center_y = 400
        self.positions = {}

    def generate_positions(self, nodes):
        next_mirrored = False
        visited_positions = []
        quadrants = [(1,1), (1,-1), (-1,-1), (-1,1)]
        quadrant_index = 0

        for i, node in enumerate(nodes):
            while True:
                # get the sign based on the quadrant rotation
                x_sign = quadrants[quadrant_index][0]
                y_sign = quadrants[quadrant_index][1]

                # get next position based on the radius
                next_pos = [self.radius*math.cos(math.radians(self.angle)), self.radius*math.sin(math.radians(self.angle))]
                
                #if its a mirrored iteration, mirror the position
                if next_mirrored:
                    next_pos[0], next_pos[1] = next_pos[1], next_pos[0]

                # get the next X and y, based on offsets and signs
                next_x = x_sign * next_pos[0] + self.center_x
                next_y = y_sign * next_pos[1] + self.center_y

                if [next_x, next_y] not in visited_positions:
                    break

                quadrant_index += 1

                if quadrant_index == 4:
                    quadrant_index = 0
                    # if it was not the mirrored iteration, set the next one
                    # to be the mirrored
                    if not next_mirrored:
                        if (next_pos[0], next_pos[1]) != (next_pos[1], next_pos[0]):
                            next_mirrored = True
                            continue

                    if next_mirrored:
                        next_mirrored = False

                    # if its already been the mirrored iteration
                    # or there was no mirror, divide the angle by two
                    self.angle /= 2
                

            visited_positions.append([next_x, next_y])

            self.positions[node.label] = {'x': next_x, 'y': next_y, 'index': i}

           
       
        return self.positions
    
    
                