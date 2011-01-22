# Importing
from __future__ import division
from time import time
print 'Tracking. Developing version.'
print
print 'Importing'

t0=time()
import matplotlib
matplotlib.use('TkAgg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
import pylab as pl
import psyco
import os

import silenus


print
print 'Using', silenus.ver
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

# Generate plotting

for i in xrange(len(centers)):
    point=centers[i]
    
    #Select i-th plot.    
    pl.scatter([x[0] for x in point], [x[1] for x in point])

print "End."
pl.show()