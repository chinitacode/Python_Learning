import time
import threading

def run(n, se):
    se.acquire()
    print("run the thread: %s" % n)
    time.sleep(1)
    se.release()

if __name__ == '__main__':
    # 设置允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run, args=(i+1,semaphore,))
        t.start()
    '''
    运行后，可以看到5个一批的线程被放行:
    run the thread: 1
    run the thread: 2
    run the thread: 3
    run the thread: 4
    run the thread: 5
    run the thread: 6
    run the thread: 7
    run the thread: 8
    run the thread: 9
    run the thread: 10
    run the thread: 11
    run the thread: 12
    run the thread: 13
    run the thread: 14
    run the thread: 15
    run the thread: 16
    run the thread: 17
    run the thread: 18
    run the thread: 19
    run the thread: 20
    '''
