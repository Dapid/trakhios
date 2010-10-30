from __future__ import division
import numpy as np
from numpy import array


print "Starting importing data"

namefile='data.txt'

file=open(namefile, 'r')
ncenters=2
centers=[]
count=0

for i in xrange(ncenters): 
    centers.append(array([]))
it=0
while True:
    #print it,
    it+=1
    line=file.readline()
    #print line
    #raw_input()
    if line=='' or line==' ':
        count+=1
        if count>5: break
    else:
        count=0
        line=line[1:-2]
        line.split('  ')
        print '*', line
        for i in xrange(ncenters):
            np.append(centers[i],float(line[i]))
            print '-', float(line[i])    
            
print

print "End"