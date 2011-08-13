from __future__ import division
import ConfigParser
import math

import numpy as np

import silenus

"""Hrun, an intelectual barbarian, is Trakhios' intelligence
core. He will analize each frame following trackable points.
"""

__version__='Hrun v.5'
config = ConfigParser.ConfigParser()
config.read('config.ini')

maxit=int(config.get('Hrun', 'maxit'))
step_tol=eval(config.get('Hrun', 'step_tol'))


class trackingPoint():
    def __init__(self, x0, datafile, tol,
                 step_tol=step_tol, maxit=maxit):
        """
        Each point, with all the logic needed to track it
        and store the data. 
        
        Parameters:
          x0: the initial value
          datafile: where to save the data
          tol: cutoff value. Under it, considered outside. 
          step_tol: convergence criterion by distance.
          maxit: convergence forced if reached.
        
        Variables
          self.radius
          self.vel
          self.x1
        
        Note on notation: x0 and x1 are vectors, not components.
        """
        
        self.x0=x0
        self.tol=tol
        self.datafile=datafile
        
        self.tol=tol
        self.step_tol=step_tol
        self.maxit=maxit
              
        # To compute
        self.radius=None
        self.vel=None
        self.xold=None 

    def find_center(self, image):
        """Finds the center of the marker in the image,
        starting from x0.
        It calls find_center_step repeatedly,
        until converged criterion is satisfied.
        """
        
        self.xold=x0
        for p in xrange(self.maxit):
            self.x1=self.find_center_step(image)
            if np.linalg.norm(self.x0-self.x1)<self.step_tol: break
            else: self.x0=self.x1

    def find_center_step(self, image):
        """Next step for find_center.
        Look for a new center starting from x0,
        iterate just once.
        
        Follow the column chord until finding the edge.
        Same with the row chord.
        The new center is the intersection of the bisections.
        
        The edge is considered when the value of the pixel is
        under tol.  
        """
 
        x=self.x0[0]
        y=self.x0[1]
        
        val=silenus.readpix(x,y,image)  # Going up in x coordinate.
        while val>self.tol:                  # Until edge is found.
            x+=1
            val=silenus.readpix(x,y,image)
        x1=x
        
        x=self.x0[0]
            
        val=silenus.readpix(x,y,image)  # Same, going down.
        while val>self.tol:
            x-=1
            val=silenus.readpix(x,y,image)
        x2=x
    
        x=self.x0[0]
    
        val=silenus.readpix(x,y,image)  # Analog process,
        while val>self.tol:                  # for y coordinate.
            y+=1
            val=silenus.readpix(x,y,image)
        y1=y
        
        y=self.x0[1]
    
        val=silenus.readpix(x,y,image)
        while val>self.tol:
            y-=1
            val=silenus.readpix(x,y,image)
        y2=y
        return np.array([(x1+x2)*0.5, (y1+y2)*0.5])    
        # The result is the mean value for each center,
        # as corresponding to a circumference.

        
    def guess_center(self):
        """NOT IMPLEMENTED
        
        Using previous information to get a better estimate of the new center.
        """
        pass
    
    def export_data(self):
        silenus.export_data(self.center, self.datafile)
    
    def velocity(self):
        self.vel=x0-xold
        
    def run(self):
        """One function to control them all, one function to wrap them all,
        One function to summon them all and the next center unveil.
        """
        
        self.find_center()
        self.export_data()
        self.velocity()

def relax(lis, r=0):
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
    
    return [math.fsum(x)/n,math.fsum(y)/n]
    
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