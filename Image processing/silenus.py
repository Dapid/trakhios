from __future__ import division
import shutil
import os

'Silenus was an old servant of the Cyclops.'
''
'He is here to assist Trakios in non-scientific heavy tasks, like file handling, as well as small uglying-code work.'

ver='Silenus v.3'

def asking_file(databasefile): # Creating saving data file.
    'Checks whether the exporting file exits.'
    'If so, it can save a copy or overwrite.'
    
    try:
        db=open(databasefile, 'r')
        db.close()
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
        databasefile=open(databasefile, 'w')
        return databasefile
    else:
        print'Do you want to save a copy of the existing data file? (y/n)',
        while True:
            cop=raw_input()
            if cop=='y' or cop=='yes':
                copy=True
                break
            elif cop=='n' or cop=='no':
                copy=False
                break
            else: print 'Command unknown. Please, type y/n.',
            
        if copy==False:
            print
            raw_input("It seems you don't want it to be executed. An error will be raised to end the program. Press enter.")
            raise 'FileHandlingError'

        elif copy==True:
            while True:
                overwrite, name=ask_overwrite()
                if overwrite==True:
                        break
                if overwrite==False:
                    print 'Try again or press Ctrl+C to terminate.'
                    print
                    
            shutil.copy(databasefile, name)
            databasefile=open(databasefile, 'w')
            return databasefile

        else: raise 'Fatal file handling error'           # This shouldn't happen.

def ask_overwrite():
    print
    name=raw_input('Please, enter the new name of the file: ')
    name=name+'.txt'
    try:
        db=open(name, 'r')
        db.close()
        print 'The file already exists. Overwrite? (y/n)',
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
    return overwrite, name
   
def readpix(x,y, image):
    'Reads the (x,y) pixel of the image.'
    'It is dimension safe, raising an error if coordinates are not valid.'
    n=len(image)
    m=len(image[0])
    if x<0 or y<0 or x>m or y>n: raise 'DimensionError. The object is outside the field.'
    val=image[y][x]
    if len(val)==1:
        return val
    else:
        #return mean(val)
        return val[0]

def mean(lis):
    s=0
    for i in lis: s+=i
    return s/len(lis)

def namefile(name, it):
    'Generates the successive name files, Vegas format.'
    return name+'_'+str(it).zfill(6)+'.png'

def export_data(data, txtfile): # Exporting data 
    "Export the coordinates of every center per fotogram."
    "The numbers are written in a row, separated by commas."
    for i in xrange(len(data)):
        for j in data[i]:
            txtfile.write(str(j))
            txtfile.write(',')
    #txtfile.write(str(data[1]))
    #txtfile.write('\n')
    txtfile.flush()
    os.fsync(txtfile.fileno())
    
def export_literal(data, txtfile): # Write data directly.
    "Writes data directly to file."
    'Used for line breaks.'
    line=str(data)
    txtfile.write(line)
    txtfile.flush()
    os.fsync(txtfile.fileno())
    
def import_data(txtfile):
    "Importes data from file"
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
