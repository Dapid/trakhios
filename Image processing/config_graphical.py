import os, glob
import ConfigParser
import time

import matplotlib
import pylab as plt
import matplotlib.image as mpimg

def input_float(mess):
    while True:
        inp=raw_input(mess)
        try:
            inp=float(inp)
            return inp
        except:
            mess='Incorrect input. Try again: '
            
def mix_channels(img, lis):
    """Mix the channels of the whole image
    
    Copied from Silenus"""
    im2=img[:,:,0]*lis[0]
    for i in xrange(1,len(img[0,0,:])):
        im2+=img[:,:,i]*lis[i]
        
    return im2

class frameStream:
    """Minimal version to load the first frame.
    """
    def __init__(self, folder):
        self.path=os.path.join(os.curdir, folder)
        self.folder=folder
        self.fails=0
        
        self.getlist()
        self.importer()
        
        
    def getlist(self):
        """Callable function."""
        self.dir=glob.glob(os.path.join(self.path,'*.png'))
        self.dir.sort()
        
        if len(self.dir)==0:
            self.isend()

    def importer(self):
        """Loads an image"""
        
        filename=self.dir[0]
        image=mpimg.imread(filename)
        
        return image
    
    def isend(self):
        if self.fails>10:
            raise IOError
        else: self.fails +=1
        
        print self.fails
        time.sleep(self.fails)
        self.getlist()
        
    def clean(self):
        for filename in self.dir:   # Now clean everything.
            try: os.remove(filename)
            except: print filename, 'not deleted.'
        
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

mode=3          # 1 for pendulums, 2 for spring.

maxit=5
step_tol=1

if mode==1:
    tol=0.7
    matrix=(-0.3,-0.3,1.6, 0)

if mode==2:
    tol=0.13
    matrix=(0.334,0.334,0.334, 0)

if mode==3:
    tol=0.4
    matrix=(0.334, 0.334, 0.334, 0)


print 'Launching.'
folder=os.path.join(os.curdir, 'MPlayer')
fStr=frameStream(folder)
print 'Importing'   
img0=fStr.importer()
m=len(img0)
n=len(img0[0])

print 'Mixing channels'

img=mix_channels(img0, matrix)
#fStr.clean()

print 'Plotting'
fig=plt.figure()

h=10
hist=3
ax=plt.subplot2grid((h,h),(0,0), rowspan=h-hist, colspan=h)
plt.title(r'$\mathrm{Image\ preview}$',size=30)
imgplot=ax.imshow(img)
imgplot.set_cmap('gist_gray') # BW colors
fig.colorbar(imgplot)

ax=plt.subplot2grid((h,h),(h-hist+1,0), colspan=h, rowspan=hist)
plt.title(r'$\mathrm{Histogram}$',size=15)
plt.hist(img.flatten(), 256, fc='k', ec='k',
         histtype='stepfilled')
plt.xlabel(r'$\mathrm{Click\ on\ the\ image\ to\ select\ '+
           'tracking\ points.\ Close\ when\ finished.}$', size=16)

pos=positions(m,n)
cid = fig.canvas.mpl_connect('button_press_event', pos.onclick)
fig.canvas.set_window_title('Trakhios::Select tracking points') 
plt.show()
fig.canvas.mpl_disconnect(cid)


# INPUT PART

tol=input_float('Please, insert the tolerance level: ')
fps=input_float('Please, insert the video fps: ')


# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', tol)
config.set(su, 'centers', pos.centers)

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
config.set(plot, 'fps', fps)

# Write
config.write(inifile)
print 'End'
