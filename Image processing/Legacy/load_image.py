import matplotlib
import pylab as plt
import matplotlib.image as mpimg

import silenus

def importer(name, it):
    print 'data/'+silenus.namefile(name, it)
    image=mpimg.imread('data/'+silenus.namefile(name, it))
    return image

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
           'tracking\ points.}$', size=16)

pos=positions(m,n)
cid = fig.canvas.mpl_connect('button_press_event', pos.onclick)
fig.canvas.set_window_title('Trakhios::Select tracking points') 
plt.show()
fig.canvas.mpl_disconnect(cid)

print 
raw_input('End ')

