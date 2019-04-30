#!./P2ENV/bin/python

from random import randint


class Die():
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        '''Create a die with sides'''
        self.num_sides = num_sides

    def roll(self):
        '''Roll the die'''
        return randint(1, self.num_sides)
