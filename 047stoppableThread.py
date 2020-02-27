import time
import threading
import queue

class StoppableThread(threading.Thread):
    """Thread class with stop_it() method. 
    The thread itself has to checks regularly for the is_stopped() condition.
    """

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stoper = threading.Event()    #class threading.Event implements event objects. 
            #An event manages a flag that can be set to true with the set() method and reset to false with the clear() method. 
            #is_set() Return true if and only if the internal flag is true.
            #The wait(timeout=None) ###not used in this example### method blocks until the flag is true. The flag is initially false.
        

    def stop_it(self):
        self._stoper.set()

    def is_stopped(self):
        return self._stoper.isSet()

timeBetweenTasks = 4 #seconds
class KindOfSheduler(StoppableThread):
    """Thread based on StoppableThread. do real work. 
    Uses queue to pause ( analog of sleep() ) thread on timeout
    when paused thread can be waken up using queue
    thread can be stopped by sending queue string message 'stop' 
    any other message just wakes up thread before timeout"""
    def __init__(self, *args, **kwargs):
        super(KindOfSheduler, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            if self.is_stopped():
                return
            ##################
            #do real work here
            
            print("Hello, world!", time.time())
            
            #end of real work!
            ##################
            try:
                task = q.get(True, timeBetweenTasks)#time.sleep(4)
            except queue.Empty:
                print('empty queue')
            else:
                print(task)
                print(type(task))
                if task == 'stop!':
                    self.stop_it()
                    

q = queue.Queue()

thread = KindOfSheduler()
print('thread before start',thread)
thread.start()
print('thread started',thread)
time.sleep(15)
q.put('do something1!')
q.put('do something2!')
q.put('do something3!')
q.put('do something4!')
q.put('stop!') #stop it using message, comment this line to test non message stop
q.put('do something6!')
q.put('do something7!')
q.put('do something8!')
time.sleep(1)
print('thread still going?',thread)
thread.stop_it() #stop it
print('thread should be stopped',thread)
thread.join()
print('thread after join',thread)
print('end')