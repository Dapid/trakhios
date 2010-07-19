'Silenus was an old servant of the Cyclops.'
''
'Here is to assist Trakios in non-scientific heavy tasks, like file handling.'


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
