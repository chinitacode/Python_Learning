'''
我们创建一个 job, 分别用 threading 和 一般的方式执行这段程序并且创建一个 list 来存放我们要处理的数据.
在 Normal 的时候, 我们这个 list 扩展4倍;
在 threading 的时候, 我们建立4个线程, 并对运行时间进行对比.
'''
import threading, copy, time
from queue import Queue

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal:         ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
    '''
    【输出结果】：
    1999998000000
    normal:          0.2830162048339844
    1999998000000
    multithreading:  0.2710154056549072

    【原因】：
    所以程序 threading 和 Normal 运行了一样多次的运算.
    但是我们发现 threading 却没有快多少,
    按理来说, 我们预期会要快3-4倍, 因为有建立4个线程,
    但是并没有. 这就是其中的 GIL 在作怪.
    '''
