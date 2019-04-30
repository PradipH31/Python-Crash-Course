#!./P2ENV/bin/python

# Imorting the pyplot module
import matplotlib.pyplot as plt

# Data to be visualized
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# Plot the data
# plot(x-axis, y-axis)
plt.plot(input_values, squares, linewidth=5)
# Set the title for the plot
plt.title("Square numbers", fontsize=24)
# Setting the label for x and y axes
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of numbers", fontsize=14)
# Modifying display of both x and y axis
plt.tick_params(axis='both', labelsize=14)
# Making the plot display
plt.show()
