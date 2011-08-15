import Queue
import threading

queue = Queue.Queue()

class thingie(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue=queue
        self.myfile='file.txt'

    def save(self, some):
        self.queue.put(some)
    
    def join(self):
        self.queue.join()
        
    def run(self):
        while True:
            data=self.queue.get()
            with open(self.myfile, 'a') as myfile:
                 myfile.write(str(data))
            self.queue.task_done()

            