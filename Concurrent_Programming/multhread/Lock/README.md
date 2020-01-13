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

E.g.
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
