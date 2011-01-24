import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import show, savefig

import silenus

def importer(name, it):
    image=mpimg.imread('data/'+silenus.namefile(name, it))
    return image


# Parameters
namecode='Try2'
n=197

frame=importer(namecode, n)
plt.imshow(frame)
plt.colorbar()

#print frame[788][137]
frame2=frame[137:140][788:790]
print frame2
plt.imshow(frame2)
plt.colorbar()


#show()
