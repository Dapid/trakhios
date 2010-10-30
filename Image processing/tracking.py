# Importing
from __future__ import division
from time import time
print 'Tracking. Developing version.'
print
print 'Importing'

t0=time()
import matplotlib
matplotlib.use('Agg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
from pylab import show, savefig
import psyco
import os

import silenus
import hrun

print
print 'Using', silenus.ver, 'and', hrun.ver
print

def importer(name, it):
    image=mpimg.imread('data/'+silenus.namefile(name, it))
    return image

t1=time()

# Setting up
tol=0.7
centers=[array([150,380]),array([520, 374])]
dbfilename='data.txt'

dbfile=silenus.asking_file(dbfilename)

t2=time()    
psyco.full()

# Parameters
namecode='try1'
bottom=0
top=203


# Iterating
print
print 'Starting'
t3=time()


for it in xrange(bottom, top+1):    # TODO: Iterate until fail.
    frame=importer(namecode, it)
    for k in xrange(len(centers)):
        centers[k]=hrun.find_center(centers[k], frame, tol)
        silenus.export(centers[k], dbfile)
    silenus.export('\n', dbfile)
    print it,
dbfile.close()
t4=time()

print 'Finished'
print
print 'Time spent:'
print str(t1-t0), 's importing modules.'
print str(t3-t2), 's setting up and compilling (user-input time excluded).'
print str(t4-t3), 's iterating, what means',str((t4-t3)/(top-bottom)) ,'s each frame.'
print
print 'That makes a total of',str(t4-t2+t1-t0) ,'s, or', str((t4-t2+t1-t0)/(top-bottom)), 's per frame.'
print 'Those stats were obtained in', str(time()-t4), 's.'
