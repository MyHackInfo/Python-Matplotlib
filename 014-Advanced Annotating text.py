import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)
# bbox_props=dict(boxstyle='roundtooth,pad=0.3',fc="cyan",ec="b",lw=2)
# ax.annotate('max', xy=(2.17, 0.61), xytext=(3, 1.5),
#                 bbox=bbox_props)


# ax.annotate('max', xy=(2.17, 0.61), xytext=(3, 1.5),
#                 arrowprops=dict(arrowstyle='->',connectionstyle='bar'))

ax.set_ylim(-2,2)
plt.show()
