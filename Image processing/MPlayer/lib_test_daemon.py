import os
import time

curr=os.curdir

print 'Launching cleaning up daemon'

while True:
    dir=os.listdir(curr)
    for item in dir:
        if '.png' in item:
            try:
                os.remove(item)
            except: pass
    time.sleep(0.2)