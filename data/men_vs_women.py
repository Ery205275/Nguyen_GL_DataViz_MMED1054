import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 6
means_women = (3, 7, 25, 101, 77, 26)
means_men = (0, 15, 25, 250, 83, 14)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, means_women, bar_width,
alpha=opacity,
color='coral',
label='Women')

rects2 = plt.bar(index + bar_width, means_men, bar_width,
alpha=opacity,
color='tan',
label='Men')

plt.xlabel('Sports')
plt.ylabel('Medals count')
plt.title('Men vs Women in each sport')
plt.xticks(index + bar_width, ('Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Skating', 'Skiing'))
plt.legend()

plt.tight_layout()
plt.show()