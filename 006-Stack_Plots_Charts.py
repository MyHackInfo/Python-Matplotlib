# Here we use plt Stack_Plots chart for show Graph.
import matplotlib.pyplot as plt

days=[1,5,10,15,20,25,30]

collage=[5,6,12,10,8,9,11]
Tv=[4,8,10,5,10,6,12]
programing=[2,6,8,12,15,13,12]


plt.stackplot(days,collage,Tv,programing,colors=['r','c','k'])

plt.title("Graph of Stack_Plots",loc='right')
plt.xlabel("X axes")
plt.ylabel("Y axes")
#plt.legend()
plt.show()
