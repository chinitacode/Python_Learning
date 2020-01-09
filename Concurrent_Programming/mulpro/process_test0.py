from multiprocessing import Process
import os

'''

# process
def run_proc(name):
    print('Process %s (%s) runs' %(name, os.getpid()))

if __name__ == "__main__":
    print('Parent process (%s) runs.' %os.getpid())
    # target 是子进程的运行程序，args是一个元祖，包含子进程运行所需参数
    p = Process(target = run_proc,args = ('test',)) #创建Process实例对象，只有调用start()方法时才生成进程
    print('Child process will start:')
    p.start()
    p.join() # join()方法等待子进程结束后再继续往下运行，通常用于进程间的同步。如果去掉了，则主进程的会先运行（下一行会先打印出来）
    print('Child process has ended.')


    # Results:
    Parent process 6136 runs.
    Child process will start:
    Process test (9136) runs
    Child process has ended.

如果要显示所涉及的各个进程的ID：
'''
def info(title):
    print(title)
    print('module name: ', __name__)
    print('parent process: ', os.getppid())
    print('process id: ', os.getpid())

def f(name):
    info('child process')
    print('hello ', name)

if __name__ == '__main__':
    info('main process')
    p = Process(target=f, args=('Vic',))
    print('child process starts')
    p.start()
    p.join()
    print('child process ends')
