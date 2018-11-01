# .title() use for title of graph.
# .xlable() use for x axes name
# .ylable() use for y axes name
# .legend() use for



import matplotlib.pyplot as plt
x = [2,4,6,8,34,5,6,7,8,9,0,34,4,6,6]
y = [8,6,4,9,45,5,7,65,53,3,4,2,55,6,7]

x1 = [2,15,12,8]
y1 = [4,8,16,12]
plt.plot(x,y,'r',label='new-data-line-')
plt.plot(x1,y1,'g',label='old-data-line')
plt.title("Graph of Data Line",loc='right')
plt.xlabel("X axes")
plt.ylabel("Y axes")
plt.legend()
plt.show()
