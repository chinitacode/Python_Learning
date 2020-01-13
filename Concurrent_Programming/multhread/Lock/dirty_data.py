'''
从以下代码的运行结果中可以看出没有锁的情况下，脏数据是如何产生的：
'''
import time, threading

number = 0

def plus():
    global number       # global声明此处的number是外面的全局变量number
    for _ in range(1000000):    # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))

for i in range(2):      # 用2个子线程，就可以观察到脏数据
    t = threading.Thread(target=plus)
    t.start()

if __name__ == '__main__':
    time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
    print("主线程执行完毕后，number = ", number)
    '''
    【运行结果】（每次数值可能都不一样）：
    子线程Thread-2运算结束后，number = 1148316
    子线程Thread-1运算结束后，number = 1214712
    主线程执行完毕后，number =  1214712

    结果并不等于2,000,000，可以很明显地看出脏数据的情况。这是因为两个线程在运行过程中，
    CPU随机调度，你算一会我算一会，在没有对number进行保护的情况下，就发生了数据错误。
    如果想获得正确结果，可以使用join()方法，让多线程变成顺序执行，如下修改代码片段：

    for i in range(2):
        t = threading.Thread(target=plus)
        t.start()
        t.join()        # 添加这一行就让两个子线程变成了同步顺序执行

    然而上面为了防止脏数据而使用join()的方法，其实是让多线程变成了单线程，属于因噎废食的做法。
    正确的做法是使用线程锁。Python在threading模块中定义了几种线程锁类，分别是：

    Lock 互斥锁
    RLock 可重入锁
    Semaphore 信号
    Event 事件
    Condition 条件
    Barrier “阻碍”
    '''
