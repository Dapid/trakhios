import subprocess, shlex
import time

t0=time.time()
vid='P.mp4'         # Source vid.
comp=3              # Compression level.

print 'Exporting to images.'
subprocess.Popen(['mplayer', vid, '-nosound', '-vo',
                  'png:z='+str(comp), '-fontconfig 0'])

tim=time.time()-t0
print 'It took', int(tim/60), 'min', tim%60, 's.'
raw_input('Finished!')