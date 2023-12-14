# import matplotlib -> kurulması gerekiyor
# Final konularına dahil değil
from matplotlib import pyplot as plt
import random

x = []

for i in range(100):
    x.append(random.randint(0,10))

w=5
y=[5,5,5,5]
for i in range(100-5+1):
    y.append(sum(x[i:i+5])/5)
    
plt.title("Random Values")
plt.plot(x, label = "data")
plt.plot(y, label = "average")
x.sort()
plt.plot(x, label = "data_sorted")
plt.legend()
plt.show()

plt.cla()
plt.bar(x, height=x)
plt.show()
plt.savefig("bar_graph.png")

#matplotlib.org