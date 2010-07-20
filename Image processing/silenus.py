from __future__ import division

'Silenus was an old servant of the Cyclops.'
''
'He is here to assist Trakios in non-scientific heavy tasks, like file handling, as well as small uglying-code work.'

print 'Silenus v.1'

def asking_file(databasefile):
    try:
        open(databasefile, 'r')
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
        raw_input('An error will be raised to end the program. Press enter.')
        raise 'FileHandlingError.'


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
