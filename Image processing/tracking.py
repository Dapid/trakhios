from __future__ import division
import time
print 'Tracking. Developing alpha version.'
print
print 'Importing'

t0=time.time()
import os
import ConfigParser
import glob

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


class frameStream:
    """Loads images from subfolder.
    
    Only attends to what there is.
    """
    def __init__(self, folder):
        self.path=os.path.join(os.curdir, folder)
        self.folder=folder
        self.getlist()
        self.cont=True
        
    def getlist(self):
        """Callable function."""
        self._dirlist_()
        
        if len(self.dir)==0:
            self.isend()

    def _dirlist_(self):
        """Get the list. Only for internal use.
        
        See getlist()."""
        self.dir=glob.glob(os.path.join(self.path,'*.png'))
        self.dir.sort()
        
    def importer(self):
        """Loads an image
        
        It is not in silenus in order to avoid
        multiple matplotlib imports"""
        
        filename=self.dir.pop(0)
        image=mpimg.imread(filename)
        os.remove(filename)

        if len(self.dir)<5:
            self.getlist()
        return image
    
    def isend(self):
        """Checks if we have reached the end of the video
        
        Current implementation just waits for it.
        """
        time.sleep(1)
        for j in xrange(3):
            self._dirlist_()
            if len(self.dir)==0:
                time.sleep(2*j)     # Wait more
            else: return None       # Exit
            
        self.cont=False
        
        
t1=time.time()
# Setting up
psyco.full()
config = ConfigParser.ConfigParser()
config.read('config.ini')

su='Setting up'
tol=float(config.get(su, 'tol'))
centers=eval(config.get(su, 'centers'))
dbfilename=config.get(su, 'dbfilename')
n=len(centers)

dbfile=silenus.asking_file(dbfilename)

t2=time.time()    

# Parameters
par='Parameters'
folder=silenus.folder

# Iterating
if __name__ == '__main__':
    print
    print 'Starting'
    print
    print 'Current time:', 
    print str(time.localtime().tm_hour)+':'+str(
                                time.localtime().tm_min)
    print
    
    centers=[hrun.trackingPoint(np.array(center),
             dbfile, tol) for center in centers]
            # Converts to arrays and calls the wrapping class.
     
    t3=time.time()
             
    Stream=frameStream(folder)
    it=1
    
    while Stream.cont==True:    # Iterate while there is left.
        frame=silenus.mix_channels(Stream.importer())
        for center in centers:
            center.run(frame)
        silenus.export_literal('\n', dbfile)
        print it,
        if it%10==0: print
        it+=1
        
    dbfile.close()
    t4=time.time()
    
    print 'Finished'
    print
    print 'Time spent:'
    print repr(t1-t0), 's importing modules.'
    print repr(t3-t2),
    print 's setting up and compiling (user-input time excluded).'
    print repr(t4-t3),
    print 's iterating, what means',
    print repr((t4-t3)/it) ,'s each frame.'
    print '(aprox.', repr(int((t4-t3)//60)), 'min).'
    print
    print 'That makes a total of',repr(t4-t2+t1-t0),
    print 's, or', repr((t4-t2+t1-t0)/it), 's per frame.'
    print 'Those stats were obtained in', repr(time.time()-t4), 's.'

raw_input('Press enter to exit. ')