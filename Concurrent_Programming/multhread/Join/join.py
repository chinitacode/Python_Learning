'''

'''
import threading, time

def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

if __name__ == '__main__':
    thread_1 = threading.Thread(target=T1_job, name='T1')
    thread_2 = threading.Thread(target=T2_job, name='T2')
    thread_1.start()
    thread_1.join()
    thread_2.start()
    print("all done\n")
    '''
    输出结果之一：
    T1 start
    T1 finish
    all done
    T2 start
    T2 finish

    或者：
    T1 start
    T1 finish
    T2 start
    all done
    T2 finish
    取决于主线程和线程2彼此的速度。

    如果只是在T2启动后加上T1，如：
    thread_1.start()
    thread_2.start()
    thread_1.join() # notice the difference!
    print("all done\n")

    则输出结果为：
    T1 start
    T2 start
    T2 finish
    T1 finish
    all done

    【原因】：
    T2在T1之后启动，并且因为T2任务量小会在T1之前完成；
    而T1也因为加了join，all done在它完成后才显示。

    也可以添加thread_2.join()进行尝试，但为了规避不必要的麻烦，
    推荐如下这种1221的V型排布：

    thread_1.start() # start T1
    thread_2.start() # start T2
    thread_2.join() # join for T2
    thread_1.join() # join for T1
    print("all done\n")

    输出结果：
    T1 start
    T2 start
    T2 finish
    T1 finish
    all done

    '''
