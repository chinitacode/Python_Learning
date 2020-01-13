import time
import queue
import threading


def worker(i):
    while True:
        item = q.get()
        if item is None:
            print("线程%s发现了一个None,可以休息了^-^" % i)
            break
        # do_work(item)做具体的工作
        time.sleep(0.5)
        print("线程%s将任务<%s>完成了！" % (i, item))
        # 做完后发出任务完成信号，然后继续下一个任务
        q.task_done()


if __name__ == '__main__':
    num_of_threads = 5

    source = [i for i in range(1, 21)]  # 模拟20个任务

    # 创建一个FIFO队列对象，不设置上限
    q = queue.Queue()
    # 创建一个线程池
    threads = []
    # 创建指定个数(5)的工作线程，并放到线程池threads中
    for i in range(1, num_of_threads+1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # 将任务源里的任务逐个放入队列
    for item in source:
        time.sleep(0.5)     # 每隔0.5秒发布一个新任务
        q.put(item)

    # 阻塞队列直到队列里的任务都完成了
    q.join()
    print("-----工作都完成了-----")
    # 停止工作线程
    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join() # 虽然是同步结束，但是因为之前线程阻塞来get queue里的任务，所以哪个线程先拿到任务是不确定的，
                 # 因此print("线程%s发现了一个None,可以休息了^-^" % i)的次序也不一样，但是线程的结束是同步的
    print(threads)
    '''
    【可能输出结果】(每次运行结果都不一样)：
    线程1将任务<1>完成了！
    线程2将任务<2>完成了！
    线程3将任务<3>完成了！
    线程4将任务<4>完成了！
    线程5将任务<5>完成了！
    线程1将任务<6>完成了！
    线程2将任务<7>完成了！
    线程3将任务<8>完成了！
    线程4将任务<9>完成了！
    线程5将任务<10>完成了！
    线程1将任务<11>完成了！
    线程2将任务<12>完成了！
    线程3将任务<13>完成了！
    线程4将任务<14>完成了！
    线程5将任务<15>完成了！
    线程1将任务<16>完成了！
    线程2将任务<17>完成了！
    线程3将任务<18>完成了！
    线程3将任务<19>完成了！
    线程5将任务<20>完成了！
    -----工作都完成了-----
    线程1发现了一个None,可以休息了^-^
    线程3发现了一个None,可以休息了^-^
    线程5发现了一个None,可以休息了^-^
    线程4发现了一个None,可以休息了^-^
    线程2发现了一个None,可以休息了^-^
    [<Thread(Thread-1, stopped 4172)>, <Thread(Thread-2, stopped 4976)>, <Thread(Thr
    ead-3, stopped 6596)>, <Thread(Thread-4, stopped 5852)>, <Thread(Thread-5, stopp
    ed 3344)>]
    '''
