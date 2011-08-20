from mplayer import Player
import time
import os

class playerStream:
    def __init__(self):
        self.p=Player(['-vo', 'png:z=3', 'P.mp4',
                       '-nosound'])#,'-fontconfig=0'])
        self.ispaused=False
    
    def pause(self):
        if not self.ispaused:
            self.p.pause()
            self.ispaused=True
            
    def resume(self):
        if self.ispaused:
            self.p.pause()
            self.ispaused=False

print 'Starting player'
vid=playerStream()
curr=os.curdir
base=len(os.listdir(curr)) #

while True:
    dir=os.listdir(curr)
    if len(dir)>base+30:
        vid.pause()
    else:
        vid.resume()
    
    time.sleep(0.2)

print 'End reached.' 
"""
print 'A'
p = Player(['-vo', 'png', 'P.mp4'])
print 'B'
raw_input()
print 'C'
p.pause()
print 'D'
raw_input('End')
"""
