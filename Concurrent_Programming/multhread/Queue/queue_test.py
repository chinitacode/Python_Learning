import threading

from queue import Queue

# 函数的参数是一个列表l和一个队列q，对列表的每个元素进行平方计算，将结果保存在队列中
def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)

# 在多线程函数中定义一个Queue，用来保存返回值，代替return
# 定义一个多线程列表，初始化一个多维数据列表，用来处理
def multithreading():
    q =Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    # 在多线程函数中定义四个线程，启动线程，将每个线程添加到多线程的列表中
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    # 分别join四个线程到主线程
    for thread in threads:
        thread.join()
    # 定义一个空的列表results，将四个线运行后保存在队列中的结果返回给空列表results
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name___=='__main__':
    multithreading()
