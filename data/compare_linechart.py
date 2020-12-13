import matplotlib.pyplot as plt
# line 1 points
y1 = [11, 12, 20, 13, 20, 17, 20, 21, 7, 20, 1, 3, 2, 4, 6, 37, 40, 49, 75, 58, 91, 90]
x1 = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
# plotting the line 1 points 
plt.plot(x1, y1, label = "Canada")
# line 2 points
y2 = [13, 14, 45, 16, 16, 30, 26, 27, 8, 7, 25, 11, 30, 9, 7, 14, 21, 34, 84, 53, 98, 65]
x2 = [1924, 1928, 1932, 1936, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1994, 1998, 2002, 2006, 2010, 2014]
# plotting the line 2 points 
plt.plot(x2, y2, label = "America")
plt.xlabel('Year')
# Set the y axis label of the current axis.
plt.ylabel('Total Medals')
# Set a title of the current axes.
plt.title('Canada vs Ameirca in the Olympic')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()