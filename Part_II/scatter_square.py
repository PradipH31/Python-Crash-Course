#!./P2ENV/bin/python

# Imorting the pyplot module
import matplotlib.pyplot as plt

# plt.scatter(x, y, s=size)
plt.scatter(2, 4, s=500)
# Modifying display of both x and y axis
plt.tick_params(axis='both', labelsize=14)

# scatter with a series of points
# use two lists of equal dimension
# plt.scatter(list_x, list_y)
x = [1, 2, 3, 5, 6]
y = [2, 5, 8, 10, 15]
plt.scatter(x, y, s=800)

# Calculating data automatically
x_val = range(100, 300)
y_val = [x**2 for x in x_val]
# Removing outline from data points and custom colors
plt.scatter(x_val, y_val, c='red', edgecolor='none', s=1)
plt.axis([0, 350, 0, 100000])

# Colormap: a series of colors
# c=y_val sets the color density
# cmap=plt.cm.* sets the colormap to be used
plt.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Reds, edgecolor='none', s=40)

# Save the plot with
# plt.savefig('file_name', bbox_inches='tight')
# bbox_inches='tight' trims extra whitespace from the plot
plt.savefig('squares_plot.png', bbox_inches='tight')

# Making the plot display
plt.show()
