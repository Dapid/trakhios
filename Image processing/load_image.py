import numpy as np
import matplotlib
import pylab as plt
import matplotlib.image as mpimg

import silenus

def importer(name, it):
    image=mpimg.imread('data/'+silenus.namefile(name, it))
    return image

def onclick(event):
        print np.array([event.xdata, event.ydata])

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

print 'Starting'
img0=importer('00', 55)
m=len(img0)
n=len(img0[0])

print 'Mixing channels'

img=silenus.mix_channels(img0)

print 'Plotting'
fig=plt.figure()

ax=fig.add_subplot(211)
plt.title(r'$\mathrm{Image\ preview}$',size=30)
imgplot=ax.imshow(img)
imgplot.set_cmap('gist_gray')
fig.colorbar(imgplot)

ax=fig.add_subplot(212)
plt.title(r'$\mathrm{Histogram}$',size=15)
plt.hist(img.flatten(), 256, fc='k', ec='k',
         histtype='stepfilled')

pos=positions(m,n)
cid = fig.canvas.mpl_connect('button_press_event', pos.onclick)
plt.show()
fig.canvas.mpl_disconnect(cid)


print
print 
print 
raw_input('End ')

