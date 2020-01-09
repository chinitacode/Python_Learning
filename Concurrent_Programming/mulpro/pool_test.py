from multiprocessing import Pool,Queue,cpu_count
import os,time,random


def task(name,results):
    start = time.time()
    print('child process %s %s() starts.' % (name, os.getpid()))
    time.sleep(random.random()*3)
    end = time.time()
    print('child process %s takes %0.2f seconds to write result %s' %(name, (end-start),name**2))
    results.put(name**2)
    print('results: ', results)

if __name__ == '__main__':
    start = time.time()
    print('Parent process (%s).' % os.getpid())
    results = Queue()
    p = Pool(4)
    for i in range(1,7):
        p.apply(task, args=(i,results,))
    p.close()
    p.join()
    end = time.time()
    print('All child processes ended. Total run time %0.2f.' %(end-start))
    print('Results: ',results)
    # Output:
    '''
    Parent process (8932).
    child process 1 8688() starts.
    child process 2 8736() starts.
    child process 3 4584() starts.
    child process 4 8484() starts.
    child process 1 takes 0.16 seconds to write result 1
    results:  [1]
    child process 5 8688() starts.
    child process 2 takes 0.40 seconds to write result 4
    results:  [4]
    child process 6 8736() starts.
    child process 5 takes 0.44 seconds to write result 25
    results:  [25]
    child process 3 takes 0.89 seconds to write result 9
    results:  [9]
    child process 4 takes 1.25 seconds to write result 16
    results:  [16]
    child process 6 takes 2.50 seconds to write result 36
    results:  [36]
    All child processes ended. Total run time 3.41.
    Results:  []

    如果把p.apply_async改成p.apply， 那就同步了，所有进程按顺序运行，总用时边长了:

    Parent process (8272).
    child process 1 8200() starts.
    child process 1 takes 1.67 seconds to write result 1
    results:  [1]
    child process 2 2176() starts.
    child process 2 takes 1.40 seconds to write result 4
    results:  [4]
    child process 3 7804() starts.
    child process 3 takes 2.03 seconds to write result 9
    results:  [9]
    child process 4 4700() starts.
    child process 4 takes 1.00 seconds to write result 16
    results:  [16]
    child process 5 8200() starts.
    child process 5 takes 2.30 seconds to write result 25
    results:  [25]
    child process 6 2176() starts.
    child process 6 takes 0.66 seconds to write result 36
    results:  [36]
    All child processes ended. Total run time 9.53.
    Results:  []
    '''
