'''
    #### About Matplotlib ####
-> Matplotlib is a plotting library for the Python programming language
    and its numerical mathematics extension NumPy.

->Original author: "John D. Hunter"
->Written in: "Python"

->How to download on Windows OS
    1->open-cmd-pip install matplotlib
    2->https://matplotlib.org/
'''

import matplotlib.pyplot as plt
# simple plot
plt.plot([1,2,3,4,5],[6,7,8,9,5])

# Extra with plot
#plt.plot([1,2,3,4,5],[6,7,8,9,5],'bo')               # 'bo','go' using blue circle markers.
#plt.plot([1,2,3,4,5],[6,7,8,9,5],'r+')               # 'r+' using red plusses.
#plt.plot([1,2,3,4,5],[6,7,8,9,5],'go--')             # 'go--' des-des-dot.
#plt.plot([1,2,3,4,5],[6,7,8,9,5],'bo',markersize=40) # Using markersize for ++ size with ,'bo','r+','go--' etc.
#plt.plot([1,2,3,4,5],[6,7,8,9,5],color='red')        # color Use for change and type of color in line.
#plt.plot([1,2,3,4,5],[6,7,8,9,5],linewidth=20)       # linewidth Use for change line width 0..N.
#plt.plot([1,2,3,4,5],[6,7,8,9,5],linestyle='dashed')  # linestyle Use for change line style .
#plt.plot([1,2,3,4,5],[6,7,8,9,5],marker='o')
plt.show()
