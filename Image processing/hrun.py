from __future__ import division
from numpy import array
import silenus

'Hrun, an intelectual barbarian, is the intelligence core of Trakhios.'
'He will analize each frame looking for trackable points.'

print 'Hrun v.1'

def find_center(x0, image, tol):
    x=x0[0]
    y=x0[1]
    it1=0
    it2=0
    it3=0
    it4=0
    
    val=silenus.readpix(x,y, image)
    #print '-', val
    while val>tol:
        x+=1
        val=silenus.readpix(x,y, image)
        it1+=1
    x1=x
    
    x=x0[0]
        
    val=silenus.readpix(x, y, image)
    #print '-', val
    while val>tol:
        x-=1
        val=silenus.readpix(x,y, image)
        it2+=1
    x2=x

    x=x0[0]

    val=silenus.readpix(x, y, image)
    #print '-', val
    while val>tol:
        y+=1
        val=silenus.readpix(x, y, image)
        it3+=1
    y1=y
    
    y=x0[1]

    val=silenus.readpix(x, y, image)
    #print '-', val
    while val>tol:
        y-=1
        val=silenus.readpix(x, y, image)
        it4+=1
    y2=y

    #print it1, it2, it3, it4
    #print '***'
    #print [(x1+x2)*0.5, (y1+y2)*0.5]
    return array([(x1+x2)*0.5, (y1+y2)*0.5])
