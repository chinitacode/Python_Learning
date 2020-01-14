# Locks of Threads 
由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。线程锁用于锁定资源，可以同时使用多个锁，当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。 


### [1. 互斥锁 Lock Objects](https://docs.python.org/3/library/threading.html#lock-objects) 
互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。使用很简单，初始化锁对象，然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。 

A primitive lock is a synchronization primitive that is not owned by a particular thread when locked.
In Python, it is currently the lowest level synchronization primitive available, implemented directly by the _thread extension module. 

A primitive lock is in one of two states, “locked” or “unlocked”.
It is created in the unlocked state. It has two basic methods, acquire() and release().
When the state is unlocked, acquire() changes the state to locked and returns immediately.
When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked,
then the acquire() call resets it to locked and returns.
The release() method should only be called in the locked state;
it changes the state to unlocked and returns immediately.
If an attempt is made to release an unlocked lock, a RuntimeError will be raised. 

Locks also support the context management protocol. 

When more than one thread is blocked in acquire() waiting for the state to turn to unlocked,
only one thread proceeds when a release() call resets the state to unlocked;
which one of the waiting threads proceeds is not defined, and may vary across implementations. 

All methods are executed atomically. 

class threading. **Lock** 
The class implementing primitive lock objects. Once a thread has acquired a lock,
subsequent attempts to acquire it block, until it is released; any thread may release it. 

Note that Lock is actually a factory function which returns an instance of the most efficient
version of the concrete Lock class that is supported by the platform. 

**acquire**(blocking=True, timeout=-1) 
Acquire a lock, blocking or non-blocking. 

When invoked with the blocking argument set to True (the default),
block until the lock is unlocked, then set it to locked and return True. 

When invoked with the blocking argument set to False, do not block.
If a call with blocking set to True would block, return **False** immediately; otherwise, set the lock to locked and return **True**. 

When invoked with the floating-point timeout argument set to a positive value,
block for at most the number of seconds specified by timeout and as long as the lock cannot be acquired.
A timeout argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is false. 

The return value is True if the lock is acquired successfully,
False if not (for example if the timeout expired). 

Changed in version 3.2: The timeout parameter is new. 

Changed in version 3.2: Lock acquisition can now be interrupted by signals on POSIX
if the underlying threading implementation supports it. 

**release**() 
Release a lock. This can be called from any thread, not only the thread which has acquired the lock. 

When the lock is locked, reset it to unlocked, and return.
If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. 

When invoked on an unlocked lock, a RuntimeError is raised. 

**There is no return value.** 

**locked**() 
Return **true** if the lock is acquired. 

E.g.1 
```
import threading

R=threading.Lock()

R.acquire() #
#R.acquire()如果这里还有一个acquire，你会发现，程序就阻塞在这里了，因为上面的锁已经被拿到了并且还没有释放的情况下，再去拿就阻塞住了
'''
对公共数据的操作
'''
R.release()
```

E.g.2 
```
import threading
import time

number = 0
lock = threading.Lock()

def plus(lk):
    global number       # global声明此处的number是外面的全局变量number
    lk.acquire()        # 开始加锁
    for _ in range(1000000):    # 进行一个大数级别的循环加一运算
        number += 1
    print("子线程%s运算结束后，number = %s" % (threading.current_thread().getName(), number))
    lk.release()        # 释放锁，让别的线程也可以访问number

if __name__ == '__main__':
    for i in range(2):      # 用2个子线程，就可以观察到脏数据
        t = threading.Thread(target=plus, args=(lock,)) # 需要把锁当做参数传递给plus函数
        t.start()
    time.sleep(2)       # 等待2秒，确保2个子线程都已经结束运算。
    print("主线程执行完毕后，number = ", number)

```

RLock的使用方法和Lock一模一样，只不过它支持重入锁。该锁对象内部维护着一个Lock和一个counter对象。counter对象记录了acquire的次数，使得资源可以被多次require。最后，当所有RLock被release后，其他线程才能获取资源。在同一个线程中，RLock.acquire()可以被多次调用，利用该特性，可以解决部分死锁问题。 


### Lock和join的区别： 
可能有疑问:既然加锁会让运行变成串行,那么我在start之后立即使用join,就不用加锁了啊,也是串行的效果啊？ 
没错，在start之后立刻使用join,肯定会将100个任务的执行变成串行,毫无疑问,最终n的结果也肯定是0,是安全的,但问题是 
start后立即join,任务内的所有代码都是串行执行的,而加锁,只是加锁的部分即修改共享数据的部分是串行的 
单从保证数据安全方面,二者都可以实现,但很明显是加锁的效率更高。 


### 2. 信号Semaphore 
类名：BoundedSemaphore 
这种锁允许一定数量的线程同时更改数据，它不是互斥锁。比如地铁安检，排队人很多，工作人员只允许一定数量的人进入安检区，其它的人继续排队。 

### 3. 事件Event 
类名：Event 

事件线程锁的运行机制：全局定义了一个Flag，如果Flag的值为False，那么当程序执行wait()方法时就会阻塞，如果Flag值为True，线程不再阻塞。这种锁，类似交通红绿灯（默认是红灯），它属于在红灯的时候一次性阻挡所有线程，在绿灯的时候，一次性放行所有排队中的线程。 

事件主要提供了四个方法set()、wait()、clear()和is_set()。 

调用clear()方法会将事件的Flag设置为False。 

调用set()方法会将Flag设置为True。 

调用wait()方法将等待“红绿灯”信号。 

is_set():判断当前是否"绿灯放行"状态 

下面是一个模拟红绿灯，然后汽车通行的例子： 
```
#利用Event类模拟红绿灯
import threading
import time

event = threading.Event()

def lighter():
    green_time = 5       # 绿灯时间
    red_time = 5         # 红灯时间
    event.set()          # 初始设为绿灯
    while True:
        print("\33[32;0m 绿灯亮...\033[0m")
        time.sleep(green_time)
        event.clear()
        print("\33[31;0m 红灯亮...\033[0m")
        time.sleep(red_time)
        event.set()

def run(name):
    while True:
        if event.is_set():      # 判断当前是否"放行"状态
            print("一辆[%s] 呼啸开过..." % name)
            time.sleep(1)
        else:
            print("一辆[%s]开来，看到红灯，无奈的停下了..." % name)
            event.wait()
            print("[%s] 看到绿灯亮了，瞬间飞起....." % name)

if __name__ == '__main__':

    light = threading.Thread(target=lighter,)
    light.start()

    for name in ['奔驰', '宝马', '奥迪']:
        car = threading.Thread(target=run, args=(name,))
        car.start()
``` 

### 3. 条件Condition 
类名：Condition 

当小伙伴a在往火锅里面添加鱼丸，这个就是生产者行为；另外一个小伙伴b在吃掉鱼丸就是消费者行为。当火锅里面鱼丸达到一定数量加满后b才能吃，这就是一种条件判断了。 
Condition称作条件锁，依然是通过acquire()/release()加锁解锁。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。 

可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。 

acquire(): 线程锁 

release(): 释放锁 

wait(timeout): 线程挂起，直到收到一个notify通知或者超时（可选的，浮点数，单位是秒s）才会被唤醒继续运行。wait()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。 

notify(n=1): 通知其他线程，那些挂起的线程接到这个通知之后会开始运行，默认是通知一个正等待该condition的线程,最多则唤醒n个等待的线程。notify()必须在已获得Lock前提下才能调用，否则会触发RuntimeError。notify()不会主动释放Lock。 

notifyAll(): 如果wait状态线程比较多，notifyAll的作用就是通知所有线程 

### 4. 定时器Timer 
class threading.Timer(interval, function, args=None, kwargs=None) 

定时器Timer类是threading模块中的一个小工具，用于指定n秒后执行某操作。一个简单但很实用的东西。 

Create a timer that will run function with arguments args and keyword arguments kwargs, after interval seconds have passed. If args is None (the default) then an empty list will be used. If kwargs is None (the default) then an empty dict will be used. 

Changed in version 3.3: changed from a factory function to a class.

cancel()
Stop the timer, and cancel the execution of the timer’s action. This will only work if the timer is still in its waiting stage.
```
from threading import Timer

def hello():
    print("hello, world")

# 表示1秒后执行hello函数
t = Timer(1, hello)
t.start()
```

### 5. 通过with语句使用线程锁 
所有的线程锁都有一个加锁和释放锁的动作，非常类似文件的打开和关闭。在加锁后，如果线程执行过程中出现异常或者错误，没有正常的释放锁，那么其他的线程会造到致命性的影响。通过with上下文管理器，可以确保锁被正常释放。其格式如下： 
```
with some_lock:
    # 执行任务...
```

这相当于： 

```
some_lock.acquire()
try:
    # 执行任务..
finally:
    some_lock.release()
```
