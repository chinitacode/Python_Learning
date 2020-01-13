import time, threading, _thread




def long_running():
    while True:
        try:
            print('Hello')
        except:
            break


def stopper(sec):
    time.sleep(sec)
    print('Exiting...')

    # this function only throws KeyboardInterrupts.
    _thread.interrupt_main()

threading.Thread(target = stopper, args = (1, )).start()

long_running()
print('Successfully interrupted~!')
