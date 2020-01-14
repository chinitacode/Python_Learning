from threading import Timer
import time

def hello(st):
    print('Thread starts.')
    print("hello, world")
    print('Thread ended.')
    print('Time used: ', time.time() - st)

if __name__ == '__main__':
    print('Main Thread starts.')
    st = time.time()
    # 表示1秒后执行hello函数
    t = Timer(2, hello,(st,))
    t.start()
    '''
    【输出结果】：
    Main Thread starts.
    Thread starts.
    hello, world
    Thread ended.
    Time used:  2.0150158405303955
    '''
