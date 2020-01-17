'''
用asyncio实现Hello world
'''
import asyncio, time

#把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
@asyncio.coroutine
def hello():
    start = time.time()
    print(f'Starting time: {start}; loop time: {loop.time()}')
    print('Hello world! Time used: %s' % (time.time()-start))
    start = time.time()
    r = yield from asyncio.sleep(1)  # 模拟IO操作，这样的休眠会阻塞当前协程但不会阻塞事件循环
    # 若在协程中需要有延时操作，应该使用 await asyncio.sleep()，而不是使用time.sleep()
    # 因为使用time.sleep()后会释放GIL，阻塞整个主线程，从而阻塞整个事件循环。
    print('Loop is running ? %s. Time used: %s'% (loop.is_running(),time.time()-start))
    print("Hello again! Time used: %s" % (time.time()-start))

if __name__ == '__main__':
    # 获取event loop:
    loop = asyncio.get_event_loop()
    # 执行coroutine:
    loop.run_until_complete(hello())
    loop.close()
    print('Loop is running ?', loop.is_running())
    '''
    Hello world! Time used: 0.0
    Loop is running ? True. Time used: 1.0000574588775635
    Hello again! Time used: 1.0000574588775635
    Loop is running ? False
    '''
