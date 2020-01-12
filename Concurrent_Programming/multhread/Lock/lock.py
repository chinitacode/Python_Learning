'''
lock在不同线程使用同一共享内存时，能够确保线程之间互不影响，
使用lock的方法是: 在每个线程执行运算修改共享内存之前，执行lock.acquire()将共享内存上锁，
确保当前线程执行时，内存不会被其他线程访问，
执行运算完毕后，使用lock.release()将锁打开， 保证其他的线程可以使用该共享内存。
'''
import threading

# 给函数一和函数二都加锁
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()

if __name__== '__main__':
    # 主函数中定义一个Lock
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    '''
    输出结果：
    job1 1
    job1 2
    job1 3
    job1 4
    job1 5
    job1 6
    job1 7
    job1 8
    job1 9
    job1 10
    job2 20
    job2 30
    job2 40
    job2 50
    job2 60
    job2 70
    job2 80
    job2 90
    job2 100
    job2 110

    【注意】：
    就算去掉t1.join()和t2.join(),输出结果仍然不变，因为t1先start所以就先抢占了资源。
    从打印结果来看，使用lock后，一个一个线程执行完。使用lock和不使用lock，最后打印输出的结果是不同的。
    '''
