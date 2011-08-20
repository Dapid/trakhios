print 'Importing'
import threading_aux as aux

print 'Launching'
t=aux.thingie()
t.setDaemon(True)
t.start()

for i in xrange(5):
    print i
    t.save(i)
t.join()

print 'Finished'