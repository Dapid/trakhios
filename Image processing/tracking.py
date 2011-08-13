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

def importer(name, it):
    image=mpimg.imread('data/'+silenus.namefile(name, it))
    return image

t1=time()

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

class tracking_point():
    def __init__(self, center, frame,datafile):
        self.center=center
        self.frame=frame
        self.tol=tol
        self.datafile=datafile
        
        # To compute
        self.radius=None
        self.vel=None

    def find_center(self):
        self.center=hrun.find_center(self.center,
                                 self.frame, self.tol).x1
    def guess_center(self):
        pass
    
    def export_data(self):
        silennus.export_data(self.center, self.datafile)
    
    def run(self):
        self.find_center()
        self.export_data()

t2=time()    


# Parameters
par='Parameters'
namecode=config.get(par, 'namecode')
top=int(config.get(par, 'top'))
bottom=int(config.get(par, 'bottom'))


# Iterating
print
print 'Starting'
t3=time()


for it in xrange(bottom, top+1):    # TODO: Iterate until fail
    frame=importer(namecode, it)
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