'''
通过继承Thread类，并重写它的run()方法来创建线程：
'''
import threading, time

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        # 注意：一定要显式的调用父类的初始化函数。
        super(MyThread, self).__init__(name = thread_name)

    def run(self):
        print("%s正在运行中......" % self.name)


class Sayhi(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    for i in range(10):
        MyThread("thread-" + str(i)).start()
    t = Sayhi('太白')
    t.start()
    print('主线程')
    '''
    【输出结果】:
    thread-0正在运行中......
    thread-1正在运行中......
    thread-2正在运行中......
    thread-3正在运行中......
    thread-4正在运行中......
    thread-5正在运行中......
    thread-6正在运行中......
    thread-7正在运行中......
    thread-8正在运行中......
    thread-9正在运行中......
    主线程
    太白 say hello
    '''
