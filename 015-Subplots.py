import random
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

fig=plt.figure()
def crete_plot():
    xs=[]
    xy=[]

    for i in range(10):
        x=i
        y = random.randrange(10)

        xs.append(x)
        xy.append(y)

    return xs,xy

## subplot2grid()
ax1=plt.subplot2grid((2,2), (0,0),rowspan=1,colspan=2)
ax2=plt.subplot2grid((2,2), (1,0),rowspan=2,colspan=1)


#### add_subplot syntax
# ax1=fig.add_subplot(211)
# ax2=fig.add_subplot(212)

x,y=crete_plot()
ax1.plot(x,y)

x,y= crete_plot()
ax2.plot(x,y)

plt.show()
