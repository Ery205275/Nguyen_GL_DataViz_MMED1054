import matplotlib.pyplot as plt

values = [386, 239]

colors = ['Tomato', 'Olive']

labels = ["Men's Total Medals", "Women Total Medals"]

explode = (0.01, 0.01)

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.title("Women vs Men Achievements", pad="20")
plt.show()