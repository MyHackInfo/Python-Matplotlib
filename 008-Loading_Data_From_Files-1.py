# Loading data from file two way
# 1-CSV file
# 2-With numpy

# 1-CSV file
'''
import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open("data.csv",'r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='loading from file')
plt.title("Loading file")
plt.legend()
plt.show()
'''

# 2-With numpy
'''
import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('data.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='loading from file')
plt.title("Loading file")
plt.legend()
plt.show()
'''
