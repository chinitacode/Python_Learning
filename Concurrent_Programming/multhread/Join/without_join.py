'''
开启多线程后不加 join() 的结果：
'''
import threading
import time

def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1) # 任务间隔0.1s
    print("T1 finish\n")

if __name__ == '__main__':
    added_thread = threading.Thread(target=thread_job, name='T1')
    added_thread.start()
    print("all done\n")

    '''
    预想中输出的结果为：
    T1 start
    T1 finish
    all done

    实际输出结果为：
    T1 start
    all done
    T1 finish

    因为没有给线程加join()来同步，所以主线程的执行与added_thread线程的执行是异步的，
    使得线程任务还未完成便在主线程里输出all done。

    若要使without_join文件里的代码按顺序输出结果，
    在print("all done\n")前加一行added_thread.join()即可。


    使用join对控制多个线程的执行顺序非常关键。
    举个例子，假设我们现在再加一个线程T2，T2的任务量较小，会比T1更快完成：

    def T1_job():
        print("T1 start\n")
        for i in range(10):
            time.sleep(0.1)
        print("T1 finish\n")

    def T2_job():
        print("T2 start\n")
        print("T2 finish\n")

    thread_1 = threading.Thread(target=T1_job, name='T1')
    thread_2 = threading.Thread(target=T2_job, name='T2')
    thread_1.start()
    thread_2.start()
    print("all done\n")

    输出结果之一为：
    T1 start
    all done
    T2 start
    T2 finish
    T1 finish
    之所以是输出结果“之一”是因为all done的出现完全取决于两个线程的执行速度，
    T2 finish完全有可能出现在all done之后。
    这种杂乱的执行方式是我们不能忍受的，因此要使用join加以控制。
    '''
