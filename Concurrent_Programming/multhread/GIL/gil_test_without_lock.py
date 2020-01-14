from threading import Thread,Lock
import os,time
def work():
    global n
    # lock.acquire() #加锁
    temp = n
    time.sleep(0.1) #一会将下面循环的数据加大并且这里的时间改的更小试试
    n = temp-1
    # time.sleep(0.02)
    # n = n - 1
    '''
    如果这样写的话看不出来效果，因为这样写就相当于直接将n的指向改了。
    就好比从10，经过1次减1之后，n就直接指向了9，速度太快，看不出效果，
    那么我们怎么办呢，找一个中间变量来接收n，然后对这个中间变量进行修改，然后再赋值给n。
    多一个给n赋值的过程，那么在这个过程中间，我们加上一点阻塞时间，来看效果，就像读文件修改数据之后再写回文件的过程。
    那么这个程序就会出现结果为9的情况，首先一个进程的全局变量对于所有线程是共享的。
    由于我们在程序给中间变量赋值，然后给n再次赋值的过程中我们加了一些I/O时间，遇到I/O就切换，
    那么每个线程都拿到了10，并对10减1了，然后大家都得到了9，然后再赋值给n，所有n等于了9。
    '''
    # lock.release()
if __name__ == '__main__':
    lock=Lock()
    n=100
    threads = [] #线程池
    for i in range(100):  #如果这里变成了10000，运行结果为76或其余非99的数
        t = Thread(target=work)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print(n) #结果为99
