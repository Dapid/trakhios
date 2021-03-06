from mplayer import Player
import time
import os

class playerStream:
    def __init__(self):
        self.p=Player(['-vo', 'png:z=3', 'Platypus.mp4',
                       '-nosound'])#,'-fontconfig=0'])
        self.ispaused=False
        self.fps=self.p.fps
        print 'Running at', self.fps, 'fps.'
        
    def pause(self):
        if not self.ispaused:
            self.p.pause()
            self.ispaused=True
            
    def resume(self):
        if self.ispaused:
            self.p.pause()
            self.ispaused=False
            
    def isend(self):
        a=self.p.stream_end
        b=self.p.stream_pos
        
        if a==None and b==None:
            return True
        else: return False

    def quit(self):
        self.p.quit()

print 'Starting player'
curr=os.curdir
base=len(os.listdir(curr))
vid=playerStream()

while True:
    dir=os.listdir(curr)
    files=len(dir)
    if files>base+30:
        vid.pause()
        time.sleep(0.2)
    else:
        vid.resume()
        time.sleep(0.5)
    
    if files==base:        # If no frames left
        if vid.isend():     # and it is the end,
            break           # exit

print 'End reached.'
vid.quit()
print 'Quitted.'
 