import ConfigParser
from numpy import array

config = ConfigParser.ConfigParser()

inifile = open('config.ini','w')

# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', 0.7)
config.set(su, 'centers', [array([150,380]),array([520, 374])])

#config.set(su, 'tol', 0.13)
#config.set(su, 'centers',[array([327,151]),array([437, 176]),array([555,180]),array([686, 168]),array([788,137])])

config.set(su, 'dbfilename', 'data.txt')

par='Parameters'
config.add_section(par)
config.set(par, 'namecode', 'try1')
config.set(par, 'bottom', 849)
config.set(par, 'top', 1093)

# Write
config.write(inifile)
print 'End'
