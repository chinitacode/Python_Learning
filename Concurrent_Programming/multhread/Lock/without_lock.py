'''
不使用lock的情况：
'''
import threading

def job1():
    global A
    for i in range(10):
        A += 1
        print('job1: %s' % A, end = '\n')

def job2():
    global A
    for i in range(10):
        A += 10
        print('job2: %s' % A, end = '\n')

if __name__== '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target = job1)
    t2 = threading.Thread(target = job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    '''
    Results:
    
    '''
