'''
[Pool]
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''

from multiprocessing import Pool,cpu_count
import os,time,random

def task(name):
    print('result is %s' %(name**2))
    return name**2

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, end-start))

if __name__ == '__main__':
    print('This computer has %s cores.' % cpu_count())
    print('Parent process (%s).' % os.getpid())
    p = Pool(4) # if not passing it paramter, the default value will be set to the number of cpu cores
    for i in range(1,7): #一下子创建6个进程，但是因为进程池容量为4，所以后两个进程要等一下
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all processes to finish...')
    p.close()
    p.join()
    print('All subprocesses done.\n')
    # Results：
    '''
    This computer has 4 cores.
    Parent process (7608).
    Waiting for all processes to finish...
    Run task 1 (8812)
    Run task 2 (8544)
    Run task 3 (8876)
    Run task 4 (5360)
    Task 3 runs 1.02 seconds
    Run task 5 (8876)
    Task 2 runs 1.10 seconds
    Run task 6 (8544)
    Task 1 runs 1.61 seconds
    Task 4 runs 1.80 seconds
    Task 6 runs 1.47 seconds
    Task 5 runs 2.64 seconds
    All subprocesses done.

    【代码注解】
    1.pool.apply_async() 采用异步的方式调用task, pool.apply() 则是同步调用，
    意味着下一个task需要等上一个task完成后才能开始运行，这不符合我们cpu并行处理的目的，
    所以采用异步方式连续第提交任务。
    2.对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
    即关闭进程池，之后就不能继续添加新的Process了。
    也可以直接用 with...as...操作：
    '''
    results = []
    with Pool(4) as p:
        for i in range(1,7):
            result = p.apply_async(long_time_task, args=(i,))
            results.append(result)
    p.join()
    print('Results: ',results)
    '''
    结果为：
    Results:  [<multiprocessing.pool.ApplyResult object at 0x02731950>, <multiproces
    sing.pool.ApplyResult object at 0x027245F0>, <multiprocessing.pool.ApplyResult o
    bject at 0x027249B0>, <multiprocessing.pool.ApplyResult object at 0x027249D0>, <
    multiprocessing.pool.ApplyResult object at 0x02724230>, <multiprocessing.pool.Ap
    plyResult object at 0x008749B0>]
    运行时long_time_task里面的print()都没打印出来，
    但是不用with...as...就可以。
    '''
