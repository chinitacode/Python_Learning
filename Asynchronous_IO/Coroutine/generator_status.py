'''
[生成器的执行状态]
生成器在其生命周期中，会有如下四个状态:

  GEN_CREATED   # 等待开始执行
  GEN_RUNNING    # 解释器正在执行（只有在多线程应用中才能看到这个状态）
  GEN_SUSPENDED  # 在yield表达式处暂停
  GEN_CLOSED     # 执行结束

'''
from inspect import getgeneratorstate

def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1

if __name__ == '__main__':
    gen = mygen(2)
    print(getgeneratorstate(gen))

    print(next(gen))
    print(getgeneratorstate(gen))

    print(next(gen))
    gen.close()  # 手动关闭/结束生成器
    print(getgeneratorstate(gen))
    '''
    【输出结果】：
    GEN_CREATED
    0
    GEN_SUSPENDED
    1
    GEN_CLOSED
    '''
