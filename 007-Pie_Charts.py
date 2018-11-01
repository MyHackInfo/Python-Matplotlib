# Here we use plt Pie-chart for show Graph.
import matplotlib.pyplot as plt
slice=[8,5,12,15,10,4]
lab=['work','gym','eating','sleeping','playing','talking']
col=['c','m','r','k','b','green']
plt.pie(slice,labels=lab,colors=col,
        startangle=90,shadow=True,
        explode=(0,0,0,0.1,0,0),
        autopct='%1.1f%%',
        pctdistance=0.6,
        labeldistance=0.8,
        radius=1.2,
        counterclock=True,
        frame=False,
        rotatelabels=False)
plt.title("Graph of Pie",loc='right')
plt.show()
