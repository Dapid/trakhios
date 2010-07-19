#importing
import numpy as np
import psyco
import matplotlib
#use Agg

print "Tracking. Developing version."

def importer(name, it):
    image=open('data/'+namefile(name, it))
    return image

def namefile(name, it):
    
def find_center(x0, image):
    
def export(data, txtfile):

def asking_file(txtfile):
    try:
        open(dbfile, 'r')
        print 'The exporting file already exists. Overwrite? (y/n)',
        while True:
            over=raw_input()
            if over=='y' or over=='yes':
                overwrite=True
                break
            elif over=='n' or over=='no':
                overwrite=False
                break
            else: print 'Command unknown. Please, type y/n.',

    except IOError: overwrite=True

    if overwrite==True:
        dbfile=open(dbfile, 'w')
        return dbfile
    else:
        raw_input('An error will be raised to end the program. Press enter.')
        raise 'FileHandlingError.'



# Setting up
tol=0.7
centers=[[20,30],[25, 49]]
dbfile='data.txt'

dbfile=asking_file(dbfile)

    
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
        
