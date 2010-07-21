from __future__ import division
from numpy import array, linalg

import silenus

'Hrun, an intelectual barbarian, is the intelligence core of Trakhios.'
'He will analize each frame looking for trackable points.'

ver='Hrun v.2 b'
maxit=5
step_tol=1


def find_center(x0, image, tol):
    x1=find_center_step(x0, image, tol)
    it=0
    for p in xrange(maxit):
        x2=find_center_step(x1, image, tol)
        if linalg.norm(x1-x2)<step_tol: break
        else: x1=x2
    return x2

    
def find_center_step(x0, image, tol):
    x=x0[0]
    y=x0[1]
    
    val=silenus.readpix(x,y, image)
    while val>tol:
        x+=1
        val=silenus.readpix(x,y, image)
    x1=x
    
    x=x0[0]
        
    val=silenus.readpix(x, y, image)
    while val>tol:
        x-=1
        val=silenus.readpix(x,y, image)
    x2=x

    x=x0[0]

    val=silenus.readpix(x, y, image)
    while val>tol:
        y+=1
        val=silenus.readpix(x, y, image)
    y1=y
    
    y=x0[1]

    val=silenus.readpix(x, y, image)
    while val>tol:
        y-=1
        val=silenus.readpix(x, y, image)
    y2=y
    return array([(x1+x2)*0.5, (y1+y2)*0.5])
