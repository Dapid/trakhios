import ConfigParser

import matplotlib
import pylab as plt
import matplotlib.image as mpimg


def mix_channels(img, lis):
    """Mix the channels of the whole image
    
    Copied from Silenus"""
    im2=img[:,:,0]*lis[0]
    for i in xrange(1,len(img[0,0,:])):
        im2+=img[:,:,i]*lis[i]
        
    return im2

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
        

class positions:
    def __init__(self, m, n):
        self.centers=[]
        self.m=m
        self.n=n
    def onclick(self, event):
        x, y=(event.xdata, event.ydata)
        if 0<=x and 0<=y and y<=self.m and x<=self.n:
            self.centers.append([x, y])
            print 'Got that!'
        else:
            print 'Invalid center. Try to click inside!'


__version__='Config_Graph v.0.1'

config = ConfigParser.ConfigParser()

inifile = open('config.ini','w')

mode=1          # 1 for pendulums, 2 for spring.

maxit=5
step_tol=1

if mode==1:
    tol=0.7
    matrix=(-0.3,-0.3,1.6, 0)

if mode==2:
    tol=0.13
    matrix=(0.334,0.334,0.334, 0)

# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', tol)
config.set(su, 'centers', centers)

config.set(su, 'dbfilename', 'data.txt')

sil='Silenus'
config.add_section(sil)
config.set(sil, 'matrix', matrix)
config.set(sil, 'folder', 'MPlayer')

hr='Hrun'
config.add_section(hr)
config.set(hr, 'maxit', maxit)
config.set(hr, 'step_tol', step_tol)

plot='Plotting'
config.add_section(plot)
config.set(plot, 'mode', mode)

# Write
config.write(inifile)
print 'End'
