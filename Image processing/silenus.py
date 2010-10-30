from __future__ import division
import shutil

'Silenus was an old servant of the Cyclops.'
''
'He is here to assist Trakios in non-scientific heavy tasks, like file handling, as well as small uglying-code work.'

ver='Silenus v.2.2.1'

def asking_file(databasefile): # Creating saving data file.
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
    n=len(image)
    m=len(image[0])
    if x<0 or y<0 or x>m or y>n: raise 'DimensionError. The object is outside the field.'
    val=image[y][x]
    if len(val)==1:
        return val
    else:
        #return mean(val)
        return val[0]

def mean(lista):
    s=0
    for i in lista: s+=i
    return s/len(lista)

def namefile(name, it):
    return name+'_'+str(it).zfill(6)+'.png'

def export(data, txtfile):
    line=str(data)+'\n'
    txtfile.write(line)
    txtfile.flush()
    os.fsync(txtfile.fileno())