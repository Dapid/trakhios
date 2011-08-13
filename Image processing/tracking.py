from __future__ import division
from time import time
print 'Tracking. Developing alpha version.'
print
print 'Importing'

t0=time()
import os
import ConfigParser

import matplotlib
matplotlib.use('Agg')           # Backend.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import psyco

import silenus
import hrun

print
print 'Using', silenus.__version__, 'and', hrun.__version__
print

t1=time()

def importer(name, it, folder):
    """Loads an image
    
    It is not in silenus in order to avoid
    multiple matplotlib imports"""
    
    image=mpimg.imread(folder+os.sep+silenus.namefile(name, it))
    #image=mpimg.imread(os.path.join(folder,
    #                silenus.namefile(name, it)))
    return image

# Setting up
psyco.full()
config = ConfigParser.ConfigParser()
config.read('config.ini')

su='Setting up'
tol=float(config.get(su, 'tol'))
centers=eval(config.get(su, 'centers'))
dbfilename=config.get(su, 'dbfilename')
n=len(centers)

centers=[np.array(each) for each in centers]

dbfile=silenus.asking_file(dbfilename)

t2=time()    


# Parameters
par='Parameters'
namecode=config.get(par, 'namecode')
top=int(config.get(par, 'top'))
bottom=int(config.get(par, 'bottom'))
folder=config.get(par, 'folder')

# Iterating
print
print 'Starting'
t3=time()


centers=[hrun.trackingPoint(center) for center in centers]

for it in xrange(bottom, top+1):    # TODO: Iterate until fail
    frame=silenus.mix_channels(importer(namecode, it, folder))
    for k in xrange(n):
        centers[k]=hrun.find_center(centers[k], frame, tol).x1
    silenus.export_data(centers, dbfile)
    silenus.export_literal('\n', dbfile)
    print it,
dbfile.close()
t4=time()

print 'Finished'
print
print 'Time spent:'
print str(t1-t0), 's importing modules.'
print str(t3-t2),
print 's setting up and compiling (user-input time excluded).'
print str(t4-t3),
print 's iterating, what means',
print str((t4-t3)/(top-bottom)) ,'s each frame.'
print
print 'That makes a total of',str(t4-t2+t1-t0),
print 's, or', str((t4-t2+t1-t0)/(top-bottom)), 's per frame.'
print 'Those stats were obtained in', str(time()-t4), 's.'
raw_input('Press enter to exit. ')