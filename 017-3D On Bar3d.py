from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax1=fig.add_subplot(111,projection='3d')


x1=[1,2,3,4,5,6,7,8,9,10]
y1=[5,6,7,8,2,5,6,3,7,2]
z1=np.zeros(10)

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

ax1.bar3d(x1,y1,z1,dx,dy,dz)
#
ax1.set_xlabel("x axis")
ax1.set_ylabel("y axis")
ax1.set_zlabel("z axis")
#
plt.show()
