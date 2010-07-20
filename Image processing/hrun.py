from __future__ import division
from numpy import array
import silenus

'Hrun, an intelectual barbarian, is the intelligence core of Trakhios.'
'He will analize each frame looking for trackable points.'

print 'Hrun v.1'

def find_center(x0, image, tol):
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
