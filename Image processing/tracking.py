#importing
from __future__ import division
import matplotlib
matplotlib.use('Agg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
from pylab import show, savefig
import psyco
import silenus
import hrun


print "Tracking. Developing version."

def importer(name, it):
    image=open('data/'+namefile(name, it))
    return image

def namefile(name, it):
    


def export(data, txtfile):



# Setting up
tol=0.7
centers=[array([20,30]),array([25, 49])]
dbfile='data.txt'

dbfile=silenus.asking_file(dbfile)

    
psyco.full()

# Parameters

namecode='test'
bottom=0
top=50


# Iterating

print 'Starting'
for it in xrange(bottom, top):
    frame=importer(namecode, it)
    for k in len(centers):
        centers[k]=hrun.find_center(centers[k], frame)
        export(centers[k], dbfile)
        
