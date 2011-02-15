import ConfigParser
from numpy import array

__version__='Config v.0.1'

config = ConfigParser.ConfigParser()

inifile = open('config.ini','w')

mode=1
bottom=850
top=900


if mode==1:
    tol=0.7
    centers=[array([150,380]),array([520, 374])]
    matrix=(0.334,0.334,0.334, 0)

if mode==2:
    tol=0.13
    centers=[array([327,151]),array([437, 176]),
         array([555,180]),array([686, 168]),array([788,137])]
    matrix=(0.334,0.334,0.334, 0)

# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', tol)
config.set(su, 'centers', centers)

config.set(su, 'dbfilename', 'data.txt')

par='Parameters'
config.add_section(par)
config.set(par, 'namecode', 'try1')
config.set(par, 'bottom', bottom)
config.set(par, 'top', top)

sil='Silenus'
config.add_section(sil)
config.set(sil, 'matrix', matrix)

plot='Plotting'
config.add_section(plot)
config.set(plot, 'mode', mode)

# Write
config.write(inifile)
print 'End'
