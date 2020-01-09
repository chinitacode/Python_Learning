from multiprocessing import Process, Queue
from wr_pid import write_pid,is_running
import os, time, random,psutil

# 写数据进程执行的代码:
def write(q):
    write_pid('pw')
    print('Process (%s) starts writing value...' %os.getpid())
    for value in ['A', 'B', 'C']:
        q.put(value)
        print ("Put %s to queue..."% value)
        time.sleep(random.random()*3)

# 读数据进程执行的代码:
def read(q):
    write_pid('pr')
    print('Process (%s) starts reading value...' %os.getpid())
    while True:
        if not q.empty():
            value = q.get(True)
            print ("Get %s from queue."% value)
            time.sleep(random.random()*3)
        else:
            print('Message queue is empty.')
            break #一旦Break出去，这个进程就结束了

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()

    is_running('pw')
    is_running('pr')

    time.sleep(3)
    is_running('pw')
    is_running('pr')

    # 等待pw结束:
    pw.join() #程序运行完后进程就会结束了
    print('Writing process ends.')
    is_running('pw')
    is_running('pr')
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    time.sleep(10)
    #pr.terminate()
    print ("所有数据都写入并且读完\n")
    '''
    (pw) is not running...
    (pr) is not running...
    Process (1708) starts writing value...
    Put A to queue...
    Process (6396) starts reading value...
    Get A from queue.
    Message queue is empty.
    Put B to queue...
    (pw) is running...
    (pr) is not running...
    Put C to queue...
    Writing process ends.
    (pw) is not running...
    (pr) is not running...
    所有数据都写入并且读完
    '''
