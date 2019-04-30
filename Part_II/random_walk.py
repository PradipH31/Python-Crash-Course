#!./P2ENV/bin/python
# Random Walk
from random import choice


class RandomWalk():
    '''A class to generate random walks'''

    def __init__(self, num_points=500):
        """Initialize attributes of a walk"""

        # num_points is the unit allowed to walk
        self.num_points = num_points

        # Walks start at 0,0 of the graph
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''The actual walk'''

        while len(self.x_values) < self.num_points:
            # x direction can be left or right i.e 1 or -1
            # choice takes any form of sequential data (string, list)
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_steps = x_direction * x_distance

            # x direction can be left or right i.e 1 or -1
            # choice takes any form of sequential data (string, list)
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_steps = y_direction * y_distance

            # Continue the loop if both x and y steps are 0
            if x_steps == 0 and y_steps == 0:
                continue

            # Take the last position of x and y and add new one
            self.x_values.append(self.x_values[-1] + x_steps)
            self.y_values.append(self.y_values[-1] + y_steps)
