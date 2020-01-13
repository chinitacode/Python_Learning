import threading, time

def thread_job():
    print('This is a thread of %s' % threading.current_thread()) # 查看现在正在运行的线程
    time.sleep(2)

def main():
    for i in range(4):
        thread = threading.Thread(target=thread_job, name='thread_job %s' %(i+1))   # 定义线程
        thread.start()  # 让线程开始工作

if __name__ == '__main__':
    main()
    print(threading.active_count()) # 获取已激活的线程数
    print(threading.enumerate()) #查看所有线程信息
    '''
   【输出结果】：
   This is a thread of <Thread(thread_job 1, started 3624)>
   This is a thread of <Thread(thread_job 2, started 4116)>
   This is a thread of <Thread(thread_job 3, started 4660)>
   This is a thread of <Thread(thread_job 4, started 7492)>
   5
   [<_MainThread(MainThread, started 7156)>, <Thread(thread_job 1, started 3624)>,
   <Thread(thread_job 2, started 4116)>, <Thread(thread_job 3, started 4660)>, <Thr
   ead(thread_job 4, started 7492)>]


    '''
