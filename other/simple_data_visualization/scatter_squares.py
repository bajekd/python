import matplotlib.pyplot as plt

''' Manually generated series of points
x_values = [1, 2, 3, 4]
y_values = [1, 4, 9, 16]
plt.scatter(x_values, y_values, s=200)
'''
''' Defining custom colors
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=(0.2, 0.5, 0.8), edgecolors='none', s=40)
'''

# Using build-in colormap
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

'''Saving plots automatically
plt.savefig('squares_plot.png', bbox_inches='tight')
'''
plt.show()