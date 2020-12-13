import matplotlib.pyplot as plt

values = [315, 203, 107]

colors = ['gold', 'silver', 'coral']

labels = ["Gold medals", "Silver medals", "Bronze medals"]

explode = (0.01, 0.01, 0.01)

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.title("Gold, Silver and Bronze medals count", pad="20")
plt.show()
