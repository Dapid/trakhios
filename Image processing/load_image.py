import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.image as mpimg
import numpy as np

import silenus

def importer(name, it):
    image=mpimg.imread('data/'+silenus.namefile(name, it))
    return image

def onclick(event):
        print np.array([event.xdata, event.ydata])

class positions:
    def __init__(self):
        self.centers=[]
    def onclick(self, event):
        self.centers.append(np.array([event.xdata, event.ydata]))

print 'Starting'
img0=importer('00', 55)
m=len(img0)
n=len(img0[0])
img=np.ones((m*n,), dtype=np.int)
img.resize(m,n)
print 'Mixing channels'
for i in xrange(m):
    for j in xrange(n):
        img[i][j]=silenus.mix_channels(img0[i][j])

print 'Plotting'
fig = plt.figure()
ax = fig.add_subplot(212)
plt.hist(img.flatten(), 256, range=(0.0,1.0), fc='k', ec='k')

ax = fig.add_subplot(211)
cax=ax.imshow(img)
fig.colorbar(cax)

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
fig.canvas.mpl_disconnect(cid)
    
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.imshow(img)
#
#pos=positions
#cid = fig.canvas.mpl_connect('button_press_event', pos.onclick)
#
#plt.show()
#fig.canvas.mpl_disconnect(cid)

print
print 
print 
raw_input('End ')

