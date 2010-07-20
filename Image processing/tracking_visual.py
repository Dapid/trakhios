# Importing
from __future__ import division
from time import time as tt
print "Tracking. Developing version."
print 'Importing'
t0=tt()
import matplotlib
matplotlib.use('Agg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy import array, dot, linalg, asarray
from pylab import show, savefig
import psyco
import os
from visual import *


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

t1=tt()

# Setting up

tol=0.7
centers=[array([300,300]),array([749, 374])]
dbfilename='data.txt'


dbfile=silenus.asking_file(dbfilename)

scene=display()
scene.title='Optical tracking.'
scene.width=500
scene.height=500
scene.autoscale=False
scene.x=100             #
scene.y=20              #
scene.fullscreen=False
scene.exit=False
srr=frame()
scene.show_rendertime=True
scene.forward=(0,0,-1)
scene.up=(0,1,0)
scene.range=(500,500,16)  #
scene.center=(500, 400, 0)

c0=curve(frame=srr,color=color.yellow, pos=centers[0], radius=3)
c1=curve(frame=srr,color=color.green, pos=centers[1], radius=3)

t2=tt()    
psyco.full()

# Parameters

namecode='firstest'
bottom=0
top=100


# Iterating

print
print
print 'Starting'
t3=tt()
for it in xrange(bottom, top+1):
    frame=importer(namecode, it)
    for k in xrange(len(centers)):
        centers[k]=hrun.find_center(centers[k], frame, tol)
        export(centers[k], dbfile)
        if k==0:
            c0.append(pos=centers[k])
        else:
            c1.append(pos=centers[k])
        
    export('\n', dbfile)
    print it,
dbfile.close()
t4=tt()

print 'Finished'
print
print 'Time spent:'
print str(t1-t0), 's importing modules.'
print str(t3-t2), 's setting up and compilling (user-input time excluded).'
print str(t4-t3), 's iterating, what means',str((t4-t3)/(top-bottom)) ,'s each frame.'
print
print 'That makes a total of',str(t4-t2+t1-t0) ,'s, or', str((t4-t2+t1-t0)/(top-bottom)), 's per frame.'
print 'Those stats were obtained in', str(tt()-t4), 's.'
