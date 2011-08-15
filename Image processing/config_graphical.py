import ConfigParser

import matplotlib
import pylab as plt
import matplotlib.image as mpimg


def namefile(name, it):
    """Generate the successive name files, Vegas format.
    
    Copied from Silenus"""
    return name+str(it).zfill(6)+'.png'

def importer(name, it):
    image=mpimg.imread('data/'+namefile(name, it))
    return image

def mix_channels(img, lis):
    """Mix the channels of the whole image
    
    Copied from Silenus"""
    im2=img[:,:,0]*lis[0]
    for i in xrange(1,len(img[0,0,:])):
        im2+=img[:,:,i]*lis[i]
        
    return im2

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

print 'Starting'

mode=1          # 1 for pendulums, 2 for spring.
bottom=1
top=4203

maxit=5
step_tol=1

folder='data'

if mode==1:
    tol=0.7
    matrix=(-0.3,-0.3,1.6, 0)


if mode==2:
    tol=0.13
    matrix=(0.334,0.334,0.334, 0)

img0=importer('00', bottom)
m=len(img0)
n=len(img0[0])
print 'Mixing channels'

img=mix_channels(img0, matrix)

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

# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', tol)
config.set(su, 'centers', pos.centers)

config.set(su, 'dbfilename', 'data.txt')

par='Parameters'
config.add_section(par)
#config.set(par, 'namecode', 'try1_')
config.set(par, 'namecode', '00')
config.set(par, 'bottom', bottom)
config.set(par, 'top', top)

sil='Silenus'
config.add_section(sil)
config.set(sil, 'matrix', matrix)
config.set(sil, 'folder', folder)

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
