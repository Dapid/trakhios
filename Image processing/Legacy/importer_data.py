from __future__ import division
import numpy as np
from numpy import array, reshape

def float_list(lis):
    newlis=[]
    for i in lis:
        newlis.append(float(i))
    return newlis

def importer_data(namefile='data.txt'):
    print "Starting importing data."
    
    file=open(namefile, 'r')
    centers=[]
    count=0
    k=0
    
    ncenters=0
    for line in file:               # Counting centers.
        if line=='\n': break
        else: ncenters+=1
    file.close()
    
    file=open(namefile, 'r')
    
    for i in xrange(ncenters): 
        centers.append(array([]))
    it=0
    while True:
        print it,
        it+=1
        line=file.readline()
        if line=='\n': pass     # Empty separator.
        elif line=='': break    # EOF
        else:
            line=line[0:-2]     # Removing \n
            line=line.split('&')
            line=float_list(line)
            centers[k]=np.append(centers[k],line, axis=0) # ...
            k+=1                # Attached as a 1D array.
            if k==ncenters: k=0
            
    print
    for k in range(ncenters):
        centers[k]=centers[k].reshape(len(centers[k])/2,2)
    file.close()
    return centers
