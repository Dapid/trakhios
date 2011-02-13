import ConfigParser
from numpy import array

config = ConfigParser.ConfigParser()

inifile = open('config.ini','w')

# set a number of parameters
su='Setting up'
config.add_section(su)
config.set(su, 'tol', 0.7)
config.set(su, 'centers', [array([150,380]),array([520, 374])])
config.set(su, 'dbfilename', 'data.txt')

par='Parameters'
config.add_section(par)
config.set(par, 'namecode', 'try1')
config.set(par, 'top', 849)
config.set(par, 'bottom', 1093)

# Write
config.write(inifile)
print 'End'
