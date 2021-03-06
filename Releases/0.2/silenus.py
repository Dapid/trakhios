from __future__ import division
import shutil
import os
import os.path
import ConfigParser



"""Silenus was an old servant of the Cyclops.

He is here to assist Trakios in non-scientific heavy tasks,
like file handling, as well as small uglying-code work.
"""

__version__='Silenus v.4'

config = ConfigParser.ConfigParser()
config.read('config.ini')
change_matrix=eval(config.get('Silenus', 'matrix'))
            # This is actually a 1D vector. I know.


def asking_file(databasefile): # Creating saving data file.
    """Check whether the exporting file exits.
    If so, it can save a copy or overwrite.
    """
    
    if os.path.exists(databasefile):
        print 'The exporting file already exists. ',
        print 'Overwrite? (y/n)',
        while True:
            over=raw_input()
            over.lower()
            if over in ('y','yes'):
                overwrite=True
                break
            elif over in ('n', 'no'):
                overwrite=False
                break
            else: print 'Option unknown. Please, type y/n.',

    else: overwrite=True

    if overwrite==True:
        databasefile=open(databasefile, 'w')
        return databasefile
    else:
        print'Do you want to save a copy of',
        print' the existing data file? (y/n)',
        
        while True:
            cop=raw_input()
            if cop=='y' or cop=='yes':
                copy=True
                break
            elif cop=='n' or cop=='no':
                copy=False
                break
            else: print 'Option unknown. Please, type y/n.',
            
        if copy==False:
            print
            print "It seems you don't want it to be ",
            print "executed. An error will be raised",
            print " to end the program. ",
            raw_input('Press enter.')
            raise 'FileHandlingError'

        elif copy==True:
            while True:
                overwrite, name=ask_overwrite()
                if overwrite==True:
                        break
                if overwrite==False:
                    print 'Try again or press Ctrl+c',
                    print 'to terminate.'
                    print
                    
            shutil.copy(databasefile, name)
            databasefile=open(databasefile, 'w')
            return databasefile

        else: raise 'Fatal file handling error' 
                                 # This shouldn't happen.

def ask_overwrite():
    print
    name=raw_input('Please, enter the new file name: ')
    name=name+'.txt'
    try:
        db=open(name, 'r')
        db.close()
        print 'The file already exists. Overwrite? (y/n)',
        while True:
            over=raw_input()
            over.lower()
            if over=='y' or over=='yes':
                overwrite=True
                break
            elif over=='n' or over=='no':
                overwrite=False
                break
            else: print 'Option unknown. Please, type y/n.',
    except IOError: overwrite=True
    return overwrite, name

def mix_channels(img, lis=change_matrix):
    """Mix the channels of the whole image"""
    im2=img[:,:,0]*lis[0]
    for i in xrange(1,len(img[0,0,:])):
        im2+=img[:,:,i]*lis[i]
        
    return im2
  

def readpix(x,y, image):
    """Read the (x,y) pixel of the image.
    
    It is dimension safe: it raises an error 
    if coordinates are not valid.
    """
    
    n=len(image)
    m=len(image[0])
    try:
        return image[y][x]
    except IndexError:
        raise IndexError('Pixel out of image')

def mean(lis):
    s=0
    for i in lis: s+=i
    return s/len(lis)

def namefile(name, it):
    """Generate the successive name files, Vegas format."""
    return name+str(it).zfill(6)+'.png'
    #TODO: choose mode: Vegas, MPlayer... if needed.
    
def export_data(data, txtfile): # Exporting data 
    """Export the coordinates of one center per a frame.
    The numbers are written in a row, separated by commas.
    
    The file buffer is flushed on export_literal, after the
    frame is completed and not here.
    """
    
    for coordinate in data:
            txtfile.write(str(coordinate))
            txtfile.write(',')

    
    
def export_literal(data, txtfile): # Write data directly.
    """Write data directly to file.
    Use it for line breaks.
    """
    
    line=str(data)
    txtfile.write(line)
    txtfile.flush()
    os.fsync(txtfile.fileno())
    
def import_data(txtfile):
    """Import data from file"""
    fil=open(txtfile)
    data=fil.readlines()
    fil.close()
    for i in xrange(len(data)):
        data[i]=data[i].split(",")[:-1]
    data2=[]
    it=0
    k=-1    # To start with 0
    for i in xrange(len(data)):
        data2.append([])
        for j in xrange(len(data[i])):
            if it%2==0:
                data2[i].append([])
                k+=1
            data2[-1][-1].append(float(data[i][j]))
            it+=1
    return data2