# Importing
from __future__ import division
print "Tracking. Developing version."
print 'Importing'
import matplotlib
matplotlib.use('Agg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
from pylab import show, savefig
import psyco
import os




print
import silenus
import hrun
print

def importer(name, it):
    image=mpimg.imread('data/'+namefile(name, it))
    return image

def namefile(name, it):
    return name+'_'+str(it).zfill(6)+'.png'

def export(data, txtfile):
    line=str(data)+'\n'
    txtfile.write(line)
    txtfile.flush()
    os.fsync(txtfile.fileno())

# Setting up
tol=0.7
centers=[array([300,300]),array([749, 374])]
dbfilename='data.txt'

dbfile=silenus.asking_file(dbfilename)

    
psyco.full()

# Parameters

namecode='firstest'
bottom=0
top=100


# Iterating

print
print
print 'Starting'
for it in xrange(bottom, top+1):
    frame=importer(namecode, it)
    for k in xrange(len(centers)):
        centers[k]=hrun.find_center(centers[k], frame, tol)
        export(centers[k], dbfile)
    export('\n', dbfile)
    print it,

print 'Finished'
