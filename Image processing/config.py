import ConfigParser
import numpy as np

__version__='Config v.0.2'

config = ConfigParser.ConfigParser()

inifile = open('config.ini','w')

mode=1          # 1 for pendulums, 2 for spring.

maxit=5
step_tol=1

if mode==1:
    tol=0.7
    centers=[[150,380],[520, 374]]
    matrix=(-0.3,-0.3,1.6, 0)
    #matrix=(0.334,0.334,0.334, 0)

if mode==2:
    tol=0.13
    centers=[[327,151],[437, 176],
         [555,180],[686, 168],[788,137]]
    matrix=(0.334,0.334,0.334, 0)

# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', tol)
config.set(su, 'centers', centers)

config.set(su, 'dbfilename', 'data.txt')

sil='Silenus'
config.add_section(sil)
config.set(sil, 'matrix', matrix)
config.set(sil, 'folder', 'MPlayer')

hr='Hrun'
config.add_section(hr)
config.set(hr, 'maxit', maxit)
config.set(hr, 'step_tol', step_tol)

plot='Plotting'
config.add_section(plot)
config.set(plot, 'mode', mode)
config.set(plot, 'fps', 25)

# Write
config.write(inifile)
print 'End'
