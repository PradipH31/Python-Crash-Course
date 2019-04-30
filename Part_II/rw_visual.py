#!./P2ENV/bin/python
# Random Walk visually

import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(10000)
rw.fill_walk()

# Colormap for the walk light color(start) to dark color(end) of the walk
# point_numbers stores the steps of the walk in order and used in c=
point_numbers = list(range(rw.num_points))

# Set the size of the plotting window.
plt.figure(figsize=(20, 9))

# Emphasize the first and last points.
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)

plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolor='none', s=15)


# Remove the axes.
plt.axis('off')

plt.show()
