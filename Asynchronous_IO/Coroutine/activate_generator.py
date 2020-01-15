'''
激活生成器主要有两个方法:
1. 使用next(generator)，即不给生成器传任何参数，
如果生成器的yield语句为 received_value = yield some_value，则received_value为None；

2. 使用generator.send(None): send括号里是传给生成器的参数，
如果生成器的yield语句只是 yield some_value, 那么send括号里则只能为None;
如果语句为 received_value = yield some_value, 则send括号里的参数会被发送给生成器后
存在received_value这个变量里。

'''
def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1

if __name__ == '__main__':
    gen = mygen(4)

    # 通过交替执行，来说明这两种方法是等价的。
    print(gen.send(None))
    print(next(gen))
    print(gen.send(None))
    print(next(gen))
    '''
    【输出结果】：
    0
    1
    2
    3
    '''
