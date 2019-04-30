#!./P2ENV/bin/python

import pygal
from random import randint
from die import Die

die = Die()
results = []
for x in range(100):
    results.append(die.roll())

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizing with pygal
hist = pygal.Bar()
hist.title = 'Result of rolling one D6 die 100 times'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)
