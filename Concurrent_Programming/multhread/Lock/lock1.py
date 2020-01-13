'''
互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。使用很简单，初始化锁对象，
然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。
'''
import threading, time



def plus():
    global number, lock       # global声明此处的number是外面的全局变量number
    lock.acquire()        # 开始加锁
    for _ in range(1000000):    # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
    lock.release()        # 释放锁，让别的线程也可以访问number

if __name__ == '__main__':
    number = 0
    lock = threading.Lock()
    for i in range(2):      # 用2个子线程，就可以观察到脏数据
        t = threading.Thread(target=plus) # 需要把锁当做参数传递给plus函数
        t.start()
    time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
    print("主线程执行完毕后，number = ", number)
    '''
    【输出结果】：
    子线程Thread-1运算结束后，number = 1000000
    子线程Thread-2运算结束后，number = 2000000
    主线程执行完毕后，number =  2000000
    '''
