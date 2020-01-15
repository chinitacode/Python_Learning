'''
注意：
consumer是一个函数，

而consumer()才是一个generator。

把一个generator传入produce后：

首先调用c.send(None)启动生成器，把None赋值给consumer函数里的n，consumer生成器返回r,即 ‘’，

但因没有print,所以不打印任何东西；

然后，一旦生产了东西，通过c.send(n)切换到consumer执行，把n发送给consumer, consumer里的n得到更新，

并从上次yield暂停的位置开始继续执行，然后yield的值传给生产者的r;

producer拿到consumer处理的结果，打印后通过循环继续生产下一条消息；

当n==5时，producer决定不生产了，通过c.close()关闭consumer这个生成器，整个过程结束。

整个流程无锁，由一个线程执行，producer和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

最后套用Donald Knuth的一句话总结协程的特点：

“子程序就是协程的一种特例。”

'''
# a generator
def consumer():
    r = ''
    while True:      # yield 后 r的值是用来return的
        n = yield r  # n的值由send传入，否则(比如直接用next(generator)调用时)为None
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def producer(c):
    c.send(None)  #预激活consumer生成器，把None赋值给consumer函数里的n，consumer生成器返回r,即 ‘’，但因没有print,所以不打印任何东西
    n = 0
    while n < 5:
        n += 1
        print('[Producer] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__ == '__main__':
    c = consumer() # consumer只是一个函数，consumer()才是生成器，即先生成生成器c
    producer(c) # 然后将生成器c传给生产者
    '''
    【输出结果】：
    [Producer] Producing 1...
    [CONSUMER] Consuming 1...
    [PRODUCER] Consumer return: 200 OK
    [Producer] Producing 2...
    [CONSUMER] Consuming 2...
    [PRODUCER] Consumer return: 200 OK
    [Producer] Producing 3...
    [CONSUMER] Consuming 3...
    [PRODUCER] Consumer return: 200 OK
    [Producer] Producing 4...
    [CONSUMER] Consuming 4...
    [PRODUCER] Consumer return: 200 OK
    [Producer] Producing 5...
    [CONSUMER] Consuming 5...
    [PRODUCER] Consumer return: 200 OK
    '''
