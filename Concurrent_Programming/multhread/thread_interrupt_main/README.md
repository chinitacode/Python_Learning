### [To interrupt the parent thread from within a child thread in python](https://stackoverflow.com/questions/39297166/is-it-possible-to-kill-the-parent-thread-from-within-a-child-thread-in-python) 
 _thread.interrupt_main (this module is called thread in Python 2.7):

```
# this function only throws KeyboardInterrupts
import time, threading, _thread

def long_running():
    while True:
        print('Hello')

def stopper(sec):
    time.sleep(sec)
    print('Exiting...')
    _thread.interrupt_main()

threading.Thread(target = stopper, args = (2, )).start()

long_running()
```
