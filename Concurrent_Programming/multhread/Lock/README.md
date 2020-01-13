# Locks of Threads 
由于线程之间的任务执行是CPU进行随机调度的，并且每个线程可能只执行了n条指令之后就被切换到别的线程了。当多个线程同时操作一个对象，如果没有很好地保护该对象，会造成程序结果的不可预期，这被称为“线程不安全”。为了保证数据安全，我们设计了线程锁，即同一时刻只允许一个线程操作该数据。线程锁用于锁定资源，可以同时使用多个锁，当你需要独占某一资源时，任何一个锁都可以锁这个资源，就好比你用不同的锁都可以把相同的一个箱子锁住是一个道理。 


### [Lock Objects](https://docs.python.org/3/library/threading.html#lock-objects) 
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
