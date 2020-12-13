import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 3
means_canada = (315, 203, 107)
means_america = (167, 319, 167)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_canada, bar_width,
alpha=opacity,
color='cyan',
label='CAN')

rects2 = plt.bar(index + bar_width, means_america, bar_width,
alpha=opacity,
color='magenta',
label='USA')

plt.xlabel('Medals count')
plt.ylabel('Canada vs America')
plt.title('Medals by country')
plt.xticks(index + bar_width, ('Gold', 'Silver', 'Bronze'))
plt.legend()

plt.tight_layout()
plt.show()