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
    job1: 1job2: 11

    job1: 12job2: 22

    job1: 23job2: 33

    job1: 34job2: 44

    job1: 45job2: 55

    job1: 56job2: 66

    job1: 67job2: 77

    job1: 78job2: 88

    job1: 89job2: 99

    job1: 100job2: 110

    可以看出结果很混乱，因为t1和t2几乎同时开始，
    t2.join()在t1.join()最后也只是使t2在t1结束后结束而已。
    '''
