'''
实现实时计算平均值
如果第一次传入10，那返回平均数自然是10.
第二次传入20，那返回平均数是(10+20)/2=15
第三次传入30，那返回平均数(10+20+30)/3=20
'''


# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激活生成器,返回0但是不打印
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()
