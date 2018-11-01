# Here we use plt Bar chart for show Graph.

import matplotlib.pyplot as plt
x = [2,4,6,8,10,12]
y = [10,12,8,6,4,2]

x1 = [3,6,9,12,15]
y2 = [15,12,9,6,3]

plt.bar(x,y,color='r',label="Bar1")
plt.bar(x1,y2,color='c',label="Bar2")

plt.title("Graph of Bar",loc='right')
plt.xlabel("X axes")
plt.ylabel("Y axes")
plt.legend()
plt.show()
