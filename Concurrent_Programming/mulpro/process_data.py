'''
进程的内存空间相互独立，所以进程间的数据是隔离的，也就是数据不共享，看下面的验证：
'''
from multiprocessing import Process
n=100 #首先我定义了一个全局变量，在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了
def work():
    global n
    n=0
    print('子进程内: ',n)

if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    p.join() #等待子进程执行完毕，如果数据共享的话，我子进程是不是通过global将n改为0了，但是你看打印结果，主进程在子进程执行结束之后，仍然是n=100，子进程n=0，说明子进程对n的修改没有在主进程中生效，说明什么？说明他们之间的数据是隔离的，互相不影响的
    print('主进程内: ',n)
    '''
    子进程内:  0
    主进程内:  100
    '''
