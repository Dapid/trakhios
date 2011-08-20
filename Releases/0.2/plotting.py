# Importing
from __future__ import division
from time import time
print 'Plotting data. Version 0.2.'
print
print 'Importing'

__version__='0.2'

t0=time()
import os
import ConfigParser

import numpy as np
import matplotlib
matplotlib.interactive(True)
matplotlib.use('TkAgg')           # Backend.
import pylab as plt
import matplotlib.image as mpimg

import silenus
import hrun

print
print 'Using', silenus.__version__, 'and', hrun.__version__
print

t1=time()
t2=time()

config = ConfigParser.ConfigParser()
config.read('config.ini')

# Parameters
dbfilename=config.get('Setting up', 'dbfilename')
mode=int(config.get('Plotting', 'mode'))

print "Importing and formatting"
# Load data
data=silenus.import_data(dbfilename)

# Reformatting data
ncenters=len(data[0])
centers=[]
for i in xrange(ncenters):
    centers.append([])

for frame in data:
    for i in xrange(ncenters):
        centers[i].append(frame[i])

#centers=hrun.relax(centers, 5)
t3=time()

# Generate plotting
fps=30

print "Plotting."
if mode==1:             # Mode 1 is for pendulum.
    fc=1
    colors=['r', 'b']
    
    fig=plt.figure(fc)
    ax=fig.add_subplot(111)
    for i in xrange(len(centers)):
        point=centers[i]
        x_coord=[x[0] for x in point]
        hrun.normalize(x_coord)
        num=len(point)
        plt.plot(np.asarray(range(num))/fps,
                        x_coord, colors[i])
        axis=list(plt.axis())                         # Axis adjustment
        axis[1]=num/fps
        plt.axis(axis)
    ax.set_title(r'$\mathrm{Both\ pendulums,\ normalized}$',
                  size=20)
    plt.xlabel(r'$\mathrm{Time\ }(s)$', size=15)
    plt.ylabel(r'$\mathrm{Horizontal\ position\ }(px)$',size=15)
    plt.savefig('X-coord_both_normalized.png')
    fig.canvas.set_window_title('Trakhios::Results') 
    
    
if mode==2:             # Mode 2 is for spring.
    colors=['r', 'b', 'g', 'c', 'y']
    for i in xrange(len(centers)):
        fc=i
        fig=plt.figure(fc)
        fig.canvas.set_window_title('Trakhios::Results') 
        ax=fig.add_subplot(111)
        point=centers[i]
          
        plt.plot(np.asarray(range(len(point)))/fps, [x[0] for x in point],
                  alpha=0.6, color=colors[i])
        axis=list(plt.axis())                         # Axis adjustment
        axis[1]=num/fps
        plt.axis(axis)
        
        ax.set_title('Spring point '+str(i+1
                        )+", dumped oscillation.")
        plt.xlabel(r'$\mathrm{Time\ }(frames)$', size=15)
        plt.ylabel(r'$\mathrm{Horizontal\ position\ }(px)$', size=15)
        plt.savefig('X-coord_'+str(i+1)+'.png')

    
    
    fc+=1
    fig=plt.figure(fc)
    fig.canvas.set_window_title('Trakhios::Results') 
    ax=fig.add_subplot(111)
    
    for i in xrange(len(centers)):
        point=centers[i]
        x_coord=[x[0] for x in point]
        x_coord=hrun.normalize(x_coord)
        plt.plot(np.asarray(range(len(point)))/fps, x_coord, colors[i],
                  alpha=0.3)
        axis=list(plt.axis())                         # Axis adjustment
        axis[1]=num/fps
        plt.axis(axis)
        
    ax.set_title('Spring, all control points.')
    plt.xlabel(r'$\mathrm{Time\ }(frames)$', size=15)
    plt.ylabel(r'$\mathrm{Horizontal\ position\ }(px)$', size=15)
    plt.savefig('X-coord_spring_all.png')
    
    
    fc+=1
    fig=plt.figure(fc)
    fig.canvas.set_window_title('Trakhios::Results') 
    ax=fig.add_subplot(111)
    
    point=centers[0]
    x_total=[x[0] for x in point]
    x_total=hrun.normalize(x_total)
    for i in xrange(1, len(centers)):
        point=centers[i]
        x_coord=[x[0] for x in point]
    
        x_coord=hrun.normalize(x_coord)
        x_total=hrun.add(x_coord, x_total)
    
    plt.plot(np.asarray(range(len(point)))/fps, x_total, alpha=0.6)
    axis=list(plt.axis())                         # Axis adjustment
    axis[1]=num/fps
    plt.axis(axis)
    ax.set_title('All spring points, normalized')
    plt.xlabel(r'$\mathrm{Time\ }(frames)$', size=15)
    plt.ylabel(r'$\mathrm{Horizontal\ position\ }(px)$', size=15)
    plt.savefig('Average.png')



t4=time()
print 'Finished'
print
print 'Time spent:'
print str(t1-t0), 's importing modules.'
print str(t2-t1), 's compiling.'
print str(t3-t2), 's loading and reformatting data.'
print str(t4-t3), 's iterating.'
print
plt.show()
