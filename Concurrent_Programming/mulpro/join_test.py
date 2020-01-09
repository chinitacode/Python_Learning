'''
join方法的例子：

让主进程在加上join的地方等待（也就是阻塞住，注意只有自己能阻塞自己），等待子进程执行完之后，再继续往下执行我的主进程，
好多时候，我们主进程需要子进程的执行结果，所以必须要等待。join感觉就像是将子进程和主进程拼接起来一样，将异步改为同步执行。

怎么样开启多个进程呢？for循环。并且我有个需求就是说，所有的子进程异步执行，
然后所有的子进程全部执行完之后，我再执行主进程，怎么搞？看代码：
'''
from multiprocessing import Process
import time,os,random

def func(i,x,y):
    print(i,x)
    time.sleep(random.random())
    print(i,y)

if __name__ == '__main__':
    print('Parent process %s runs. ' %os.getpid())
    # list of all child processes
    p_list = []
    for i in range(6):
        p = Process(target=func,args=(i,'Hello', 'World'))
        p_list.append(p)
        p.start()
        #print(p.name)
        #p.join()
    #p.join()
    [ap.join() for ap in p_list]
    print('Parent process testing')




    '''
    1.如果主进程（父进程）和所有子进程之间不安排任何同步机制，全部异步运行的话，
    父进程和主进程是“同时”运行的。

    #如果func里不注释掉time.sleep()，因为打印y会被睡眠阻塞，
    所以x全部先被打印出来，即阻塞时有进程之间的切换。Output为：
    ----------------------------
    Parent process 10168 runs.
    Parent process testing
    0 Hello
    3 Hello
    2 Hello
    1 Hello
    3 World
    4 Hello
    5 Hello
    0 World
    5 World
    4 World
    2 World
    1 World
    ----------------------------
    #如果func里注释掉time.sleep(), 子进程运行时则都是先打印一个x然后一个y，
    因为两个打印距离太近了而且执行的也非常快
    所以output为：
    ----------------------------
    Parent process 9740 runs.
    Parent process testing
    4 Hello
    4 World
    1 Hello
    1 World
    3 Hello
    3 World
    2 Hello
    2 World
    5 Hello
    5 World
    0 Hello
    0 World
    ----------------------------
    2.如果在for循环外添加一个p.join(),则主进程的程序仍然比一些子进程先执行完，
    因为我们p.join()是对最后一个子进程(即i为5的子进程)进行了join，也就是说如果这最后一个子进程先于其他子进程执行完，
    那么主进程就会去执行，而此时如果还有一些子进程没有执行完，而主进程执行完了，那么就会先打印主进程的内容了，

    （这个和cpu调度进程的机制有关系，因为我们的电脑可能只有4个cpu，我的子进程加上住进程有7个，
    虽然我for循环是按顺序起进程的，但是操作系统一定会按照顺序给你执行你的进程吗，答案是不会的，
    操作系统会按照自己的算法来分配进程给cpu去执行，
    这里也解释了我们打印出来的子进程中的内容也是没有固定顺序的原因，
    因为打印结果也需要调用cpu，可以理解成进程在争抢cpu。）
    ----------------------------
    #Output:
    0 Hello
    0 World
    2 Hello
    2 World
    3 Hello
    3 World
    1 Hello
    1 World
    5 Hello
    5 World
    Parent process testing  #因为p.join()里的p对应的是for循环的最后一个i=5时的子进程。
    4 Hello
    4 World
    ----------------------------
    3.如果p.join()加到for循环里面，那么所有子进程包括父进程就全部变为同步了，
    因为for循环也是主进程的，循环第一次的时候，一个进程去执行了，然后这个进程就join住了，
    那么for循环就不会继续执行了，等着第一个子进程执行结束才会继续执行for循环去创建第二个子进程。
    ----------------------------
    #Output:
    Parent process 9276 runs.
    0 Hello
    0 World
    1 Hello
    1 World
    2 Hello
    2 World
    3 Hello
    3 World
    4 Hello
    4 World
    5 Hello
    5 World
    Parent process testing
    ----------------------------
    4.在for循环外加[ap.join() for ap in p_list]，这是解决办法，
    前提是我们的子进程全部都已经去执行了，那么我在一次给所有正在执行的子进程加上join，
    那么主进程就需要等着所有子进程执行结束才会继续执行自己的程序了，并且保障了所有子进程是异步执行的。
    ----------------------------
    #Output:
    Parent process 9664 runs.
    3 Hello
    3 World
    2 Hello
    1 Hello
    1 World
    2 World
    0 Hello
    0 World
    4 Hello
    4 World
    5 Hello
    5 World
    Parent process testing
    ----------------------------
    如果再取消func里对睡眠的注释，子进程输出结果会更异步（更乱）：
    Parent process 10204 runs.
    1 Hello
    2 Hello
    0 Hello
    4 Hello
    3 Hello
    3 World
    5 Hello
    1 World
    5 World
    0 World
    2 World
    4 World
    Parent process testing
    ----------------------------
    '''
