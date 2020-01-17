'''
从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：

把@asyncio.coroutine替换为async；
把yield from替换为await。


新语法：
'''
import asyncio, time

#把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
async def hello():
    start = time.time()
    print(f'Starting time: {start}; loop time: {loop.time()}')
    print('Hello world! Time used: %s' % (time.time()-start))
    start = time.time()
    r = await asyncio.sleep(1)  # 模拟IO操作，这样的休眠会阻塞当前协程但不会阻塞事件循环
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
    Starting time: 1579155161.4402308; loop time: 16572.797
    Hello world! Time used: 0.0
    Loop is running ? True. Time used: 1.0000572204589844
    Hello again! Time used: 1.0000572204589844
    Loop is running ? False
    '''
