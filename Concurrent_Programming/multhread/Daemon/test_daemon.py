'''
如果你设置一个线程为守护线程，，就表示你在说这个线程是不重要的，在进程退出的时候，不用等待这个线程退出。
如果你的主线程在退出的时候，不用等待那些子线程完成，那就设置这些线程的daemon属性。
即，在线程开始（thread.start()）之前，调用setDeamon（）函数，设定线程的daemon标志。
（thread.setDaemon(True)）就表示这个线程“不重要”。

如果你想等待子线程完成再退出，那就什么都不用做。
或者显示地调用thread.setDaemon(False)，设置daemon的值为false。
新的子线程会继承父线程的daemon标志。
主线程会在所有的非守护线程退出后才会结束，即进程中没有非守护线程存在的时候才结束。

'''

from threading import Thread
import time

def hello(name):
    print('%s says hello.' % name)
    time.sleep(2)
    print('Thread ended.')

if __name__ == '__main__':
    # 不设置为守护线程的情况：
    # print('主线程')
    # t = Thread(target = hello, args = ('Nick',))
    # t.start()
    # #time.sleep(3)
    # print(t.is_alive())
    # print('主线程结束')
    '''
    【输出结果】：
    主线程
    Nick says hello.
    True
    主线程结束
    Thread ended.
    '''

    # 开启守护线程
    print('主线程')
    t1 = Thread(target = hello, args = ('Nick',), daemon = True)  # 等同于单独设置t1.setDaemon(True)
    t1.start()
    print(t1.is_alive())
    print('主线程结束')
    '''
    【输出结果】：
    主线程
    Nick says hello.
    True
    主线程结束

    【Note】:
    可看出设置为了守护线程后，线程虽然未运行完毕，但是在主线程结束后也就结束了。
    并未来得及打印'Thread ended.'。
    '''
