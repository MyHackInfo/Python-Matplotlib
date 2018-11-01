# Here we use plt Histpgrams chart for show Graph.

import matplotlib.pyplot as plt
x = [10,18,20,22,26,30,35,40,43,55,59,64,70,85,82,78,100,104,115,122]


bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]


plt.hist(x,bins,histtype='bar',rwidth=0.8,color='r',label="Hist1")


plt.title("Graph of Hist",loc='right')
plt.xlabel("X axes")
plt.ylabel("Y axes")
plt.legend()
plt.show()
