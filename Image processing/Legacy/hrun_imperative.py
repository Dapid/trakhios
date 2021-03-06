from __future__ import division
from numpy import array, linalg

import silenus

"""Hrun, an intelectual barbarian, is Trakhios' intelligence
core. He will analize each frame following trackable points.
"""

__version__='Hrun v.4'
maxit=5
step_tol=1


def find_center(x0, image, tol, step_tol=step_tol):
    """Finds the center of the marker in the image,
    starting from x0.
    It calls find_center_step repeteadly,
    until converged criterion is satisfied.
    """
    
    for p in xrange(maxit):
        x1=find_center_step(x0, image, tol)
        if linalg.norm(x0-x1)<step_tol: break
        else: x0=x1
    return x1

    
def find_center_step(x0, image, tol):
    """Next step for find_center.
    Look for a new center starting from x0,
    iterate just once.
    
    Follow the column chord until finding the edge.
    Same with the row chord.
    The new center is the intersection of the bisections.
    
    The edge is considered when the value of the pixel is
    under tol.  
    """
    
    x=x0[0]
    y=x0[1]
    
    val=silenus.readpix(x,y,image)  # Going up in x coordinate.
    while val>tol:                  # Until edge is found.
        x+=1
        val=silenus.readpix(x,y, image)
    x1=x
    
    x=x0[0]
        
    val=silenus.readpix(x,y,image)  # Same, going down.
    while val>tol:
        x-=1
        val=silenus.readpix(x,y, image)
    x2=x

    x=x0[0]

    val=silenus.readpix(x,y,image)  # Analog process,
    while val>tol:                  # for y coordinate.
        y+=1
        val=silenus.readpix(x,y,image)
    y1=y
    
    y=x0[1]

    val=silenus.readpix(x, y, image)
    while val>tol:
        y-=1
        val=silenus.readpix(x, y, image)
    y2=y
    return array([(x1+x2)*0.5, (y1+y2)*0.5])    
    # The result is the mean value for each center,
    # as corresponding to a circumference.

def relax(lis, r):
    """Promediates over a series of points
     in order to reduce noise.
    """                             # TODO
    
    return lis  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    if r==0:        # Nothing to do
        return lis
    
    lis2=[]
    lis3=[]
    centers=len(lis)
    points=len(lis[0])-2*r
    
    for i in xrange(points):
        lis3.append([])
    for i in xrange(centers):
        lis2.append(lis3)
    del(lis3)
    
    for i in xrange(centers):
        for j in xrange(points):
            lis2[i][j]=promediate(lis[i][j:j+2*r], r)
    return lis2

def promediate(lis, n):
    x=[x[0] for x in lis]
    y=[x[1] for x in lis]
    
    return [sum(x)/n,sum(y)/n]
    
def add_lists(lis1, lis2):
    """Sum two lists."""
    return [i+j for i,j in zip(list1, list2)]


def normalize(lis):
    """Displace numbers in a list, now its mean is 0."""
    
    m=0
    for i in lis:
        m+=i
    m=m/len(lis)
    
    for i in xrange(len(lis)): # Could be list comprehension.
        lis[i]-=m
    return lis