# Importing
from __future__ import division
from time import time
print 'Plotting data. Developing version.'
print
print 'Importing'

t0=time()
import matplotlib
matplotlib.use('TkAgg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
import psyco
import os

import silenus
import hrun


print
print 'Using', silenus.ver, 'and', hrun.ver
print

# Parameters
dbfilename='data.txt'

# Load data
data=silenus.import_data(dbfilename)

# Reformatting data
ncenters=len(data[0])
centers=[]
for i in xrange(ncenters):
    centers.append([])

for frame in data:
    for i in xrange(ncenters):
        centers[i].append(frame[i])

centers=hrun.relax(centers, 5)

# Generate plotting
for i in xrange(len(centers)):
    fig=plt.figure(i)
    ax=fig.add_subplot(111)
    point=centers[i]
    
    plt.scatter([x[0] for x in point], [x[1] for x in point], alpha=0.4)   
    plt.plot([x[0] for x in point], [x[1] for x in point], alpha=0.3)
    
    ax.set_title('Center '+str(i+1)+".")
    plt.xlabel('px')
    plt.ylabel('px')
    plt.savefig(str(i)+'th.png')
    
print "End."
plt.show()