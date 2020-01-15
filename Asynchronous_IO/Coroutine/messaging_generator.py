'''
[从生成器过渡到协程：yield]
生成器为我们引入了暂停函数执行（yield）的功能。当有了暂停的功能之后，
人们就想能不能在生成器暂停的时候向其发送一点东西（其实上面也有提及：send(None)）。
这种向暂停的生成器发送信息的功能通过 PEP 342 进入 Python 2.5 中，并催生了 Python 中协程的诞生。

从本质上而言，协程并不属于语言中的概念，而是编程模型上的概念。
协程和线程，有相似点，多个协程之间和线程一样，只会交叉串行执行；
也有不同点，线程之间要频繁进行切换，加锁，解锁，从复杂度和效率来看，和协程相比，这确是一个痛点。
协程通过使用 yield 暂停生成器，可以将程序的执行流程交给其他的子程序，从而实现不同子程序的之间的交替执行。

下面通过一个简明的演示来看看，如何向生成器中发送消息。
'''
# 在范围N内跳跃
def jumping_range(N):
    index = 0
    while index < N:
        # 通过send()发送的信息将赋值给jump
        jump = yield index  #生成器通过yield返回index
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    itr = jumping_range(5) # 生成跳跃范围为5的生成器iter
    print(next(itr)) # 不给iter传入任何参数来激活iter，则默认传入None赋值给yield前面的变量
    print(itr.send(2))
    print(next(itr))
    print(itr.send(-1))
    '''
    【输出结果】：
    0
    2
    3
    2

    【原因】：
    重点分析jump = yield index这个语句，
    可分成两部分：
    yield index 是将index return给外部调用程序。
    jump = yield 可以接收外部程序通过send()发送的信息，并赋值给jump
    '''
