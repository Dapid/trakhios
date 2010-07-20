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
import os
import silenus
import hrun


print "Tracking. Developing version."

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
centers=[array([230,230]),array([374, 749])]
dbfilename='data.txt'

#dbfile=silenus.asking_file('data.txt')
dbfile=open(dbfilename, 'w')
    
psyco.full()

# Parameters

namecode='firstest'
bottom=0
top=50


# Iterating

print 'Starting'
for it in xrange(bottom, top):
    frame=importer(namecode, it)
    for k in xrange(len(centers)):
        centers[k]=hrun.find_center(centers[k], frame, tol)
        export(centers[k], dbfile)
    export('\n', dbfile)
    print it

print 'Finished'
