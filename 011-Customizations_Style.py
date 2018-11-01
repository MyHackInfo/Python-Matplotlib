# Here we use plt scatter chart for show Graph.

import matplotlib.pyplot as plt
from matplotlib import style
x = [2,4,6,8,10,12]
y = [10,12,8,6,4,2]

x1 = [3,6,9,12,15]
y2 = [15,12,9,6,3]

# style 'ggplot',"dark_background",'fivethirtyeight'
style.use('ggplot')

plt.scatter(x,y,color='r', label="scatter1")
plt.scatter(x1,y2,color='c',label="scatter2")

plt.title("Graph of scatter",loc='right')
plt.xlabel("X axes")
plt.ylabel("Y axes")
plt.legend()
plt.show()
