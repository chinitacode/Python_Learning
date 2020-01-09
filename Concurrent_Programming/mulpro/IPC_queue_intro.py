from multiprocessing import Queue

'''
以消息队列的方式实现进程间通信，
消息队列使用Intro：

初始化Queue()对象时（例如：q=Queue()），若括号中没有指定最大可接收的消息数量，或数量为负值，
那么就代表可接受的消息数量没有上限（直到内存的尽头）；

-Queue.qsize()：返回当前队列包含的消息数量；
-Queue.empty()：如果队列为空，返回True，反之False ；
-Queue.full()：如果队列满了，返回True,反之False；

-Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；

1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），
直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；

-Queue.get_nowait()：相当Queue.get(False)；

-Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True；

1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，
此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，如果设置了timeout，
则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；

2）如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；

-Queue.put_nowait(item)：相当Queue.put(item, False)；
'''


q = Queue(3)
for i in range(3):
    q.put('Message %s' %i)
print('Is message queue full? ',q.full())
print(q,'\n')

try:
    for i in range(3,6):
        q.put('Message %s' %i, True, 2) #会等待2秒，如果消息队列还没有空间写入则抛出异常
except:
    print('Message queue is now full with %s messages: \n' %q.qsize())
    #for i in range(q.qsize()):
        #print(q.get())

try:
    for i in range(3,6):
        q.put_nowait('Message %s' %i) #立刻抛出异常，相当于Queue.put_nowait(item)
except:
    print('Message queue is now full with %s messages: \n' %q.qsize())

#推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

#读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())

#print(q.get(True,2)) #此时程序将被阻塞（停在读取状态）2s,若还没读取到任何消息，则抛出"Queue.Empty"异常
#print(q.get(False)) #相当于Queue.get_nowait()，消息列队如果为空，则会立刻抛出"Queue.Empty"异常

print('Is message queue full? ',q.full())
