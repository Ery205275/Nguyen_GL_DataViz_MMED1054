import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Biathlon', 'Bobsleigh', 'Curling', 'Ice Hockey', 'Skating', 'Skiing')
y_pos = np.arange(len(objects))
performance = [3, 22, 50, 351, 159, 40]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Medals Count Of Each Sports')

plt.show()