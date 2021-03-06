import ConfigParser
from numpy import array

__version__='Config v.0.1'

config = ConfigParser.ConfigParser()

inifile = open('config.ini','w')

mode=1          # 1 for pendulums, 2 for spring.
bottom=54
top=136

maxit=5
step_tol=1

if mode==1:
    tol=0.7
    centers=[array([150,380]),array([520, 374])]
    matrix=(-0.3,-0.3,1.6, 0)
    #matrix=(0.334,0.334,0.334, 0)

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
#config.set(par, 'namecode', 'try1_')
config.set(par, 'namecode', '00')
config.set(par, 'bottom', bottom)
config.set(par, 'top', top)

sil='Silenus'
config.add_section(sil)
config.set(sil, 'matrix', matrix)

hr='Hrun'
config.add_section(hr)
config.set(hr, 'maxit', maxit)
config.set(hr, 'step_tol', step_tol)

plot='Plotting'
config.add_section(plot)
config.set(plot, 'mode', mode)

# Write
config.write(inifile)
print 'End'
