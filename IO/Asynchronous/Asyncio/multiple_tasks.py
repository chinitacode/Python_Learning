import threading
import asyncio

@asyncio.coroutine
def task(num):
    print(f'Task {num} starts, corresponding to {threading.currentThread()}')
    yield from asyncio.sleep(1)
    print(f'Task {num} starts, corresponding to {threading.currentThread()}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [task(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    '''
    Task 0 starts, corresponding to <_MainThread(MainThread, started 8728)>
    Task 2 starts, corresponding to <_MainThread(MainThread, started 8728)>
    Task 1 starts, corresponding to <_MainThread(MainThread, started 8728)>
    (暂停约1秒)
    Task 0 starts, corresponding to <_MainThread(MainThread, started 8728)>
    Task 2 starts, corresponding to <_MainThread(MainThread, started 8728)>
    Task 1 starts, corresponding to <_MainThread(MainThread, started 8728)>

    由打印的当前线程名称可以看出，3个coroutine是由同一个线程并发执行的。
    如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
    '''


'''
# 等同于：
async def task(num):
    print(f'Task {num} starts, corresponding to {threading.currentThread()}')
    await asyncio.sleep(1)
    print(f'Task {num} starts, corresponding to {threading.currentThread()}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [task(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
'''
