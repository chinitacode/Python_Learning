from multiprocessing import Manager,Pool
import os,time,random

def reader(q):
    print("Process reader (%s) 启动, 父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))

def writer(q):
    print("Process writer (%s) 启动,父进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "Hello world!":
        q.put(i)

if __name__=="__main__":
    print("(%s) starts"%os.getpid())
    q=Manager().Queue() #使用Manager中的Queue来初始化
    p=Pool(4)
    #使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
    p.apply(writer,(q,))
    p.apply(reader,(q,))
    p.close()
    p.join()
    print("(%s) ends"%os.getpid())
