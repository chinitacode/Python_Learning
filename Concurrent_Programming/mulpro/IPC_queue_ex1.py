from multiprocessing import Process, Queue
from wr_pid import write_pid,is_running
import os, time, random
'''
用消息队列实现两个进程（一个写进程一个读进程）之间的通信：
'''


#写数据进程执行代码：
def write(q,num):
    write_pid('pw')
    print('Process to write: %s' % os.getpid())
    for value in range(num):
        s = time.time()
        print('Writing value %s to queue... ' % value)
        time.sleep(random.random()*3)
        q.put(value)
        e = time.time()
        print('Finish writing value %s to queue, time taken: %0.2fs' %(value,e-s))

#读数据进程执行代码：
def read(q):
    write_pid('pr')
    print('Process to read: %s' % os.getpid())
    #会一直读下去
    while True:
        s = time.time()
        print('Reading value...')
        value = q.get() #没有设置timeout（单位秒），若消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止
        time.sleep(random.random()*3)
        e = time.time()
        print('Value %s read, time taken: %0.2fs' %(value,(e-s)))

if __name__ == '__main__':
    #父进程创建消息队列，并传给各个子进程：
    q = Queue(3)
    pw = Process(target=write, args=(q,3,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw,写入：
    pw.start()
    #启动子进程pr，读取：
    pr.start()
    is_running('pw')
    is_running('pr')
    #等待pw结束：
    pw.join()
    print('Is writing process alive?', pw.is_alive())
    is_running('pw')
    is_running('pr')
    time.sleep(5) #等待pr读完最后一个数据
    #pr进程是死循环，若无消息读取，会一直阻塞自己，只能强制终止：
    print('Is reading process alive?', pr.is_alive())
    is_running('pw')
    is_running('pr')
    pr.terminate()
    print('Main Process kills the reading process')
    print('Is reading process alive?', pr.is_alive())
    is_running('pw')
    is_running('pr')
    print('Is reading process alive?', pr.is_alive())
    print('All data have been written and read.')
    print('Is reading process alive?', pr.is_alive())
    # Output:
    '''
    (pw) is not running...
    (pr) is running...
    Process to write: 1432
    Writing value 0 to queue...
    Process to read: 8936
    Reading value...
    Finish writing value 0 to queue, time taken: 2.28s
    Writing value 1 to queue...
    Finish writing value 1 to queue, time taken: 0.91s
    Writing value 2 to queue...
    Finish writing value 2 to queue, time taken: 0.40s
    Is writing process alive? False
    (pw) is not running...
    (pr) is running...
    Value 0 read, time taken: 5.05s
    Reading value...
    Value 1 read, time taken: 1.10s
    Reading value...
    Value 2 read, time taken: 0.50s
    Reading value...
    Is reading process alive? True
    (pw) is not running...
    (pr) is running...
    Main Process kills the reading process
    Is reading process alive? True
    (pw) is not running...
    (pr) is not running...
    Is reading process alive? False
    All data have been written and read.
    Is reading process alive? False

    '''
