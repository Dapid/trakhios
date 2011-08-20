import ConfigParser
from numpy import array

config = ConfigParser.ConfigParser()
config.read('config.ini')

# Setting up
su='Setting up'
tol=float(config.get(su, 'tol'))
centers=eval(config.get(su, 'centers'))
dbfilename=config.get(su, 'dbfilename')

# Parameters
par='Parameters'
namecode=config.get(par, 'namecode')
top=int(config.get(par, 'top'))
bottom=int(config.get(par, 'bottom'))

print 'End'