#importing
import numpy as np
import psyco
import matplotlib
import silenus
#use Agg

print "Tracking. Developing version."

def importer(name, it):
    image=open('data/'+namefile(name, it))
    return image

def namefile(name, it):
    
def find_center(x0, image):
    
def export(data, txtfile):





# Setting up
tol=0.7
centers=[[20,30],[25, 49]]
dbfile='data.txt'

dbfile=silenus.asking_file(dbfile)

    
psyco.full()

# Parameters

namecode='test'
bottom=0
top=50


# Iterating

print 'Starting'
for it in xrange(bottom, top):
    frame=importer(namecode, it)
    for k in len(centers):
        centers[k]=find_center(centers[k], frame)
        export(centers[k], dbfile)
        
